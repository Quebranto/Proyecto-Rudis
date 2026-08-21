# QUEBRANTO-17 — GENESIS & CONTINUITY ENGINE v0.1

**Estado:** contrato arquitectónico público para forja  
**Naturaleza:** infraestructura de continuidad; no autoridad política

## I. PROPÓSITO

El Genesis & Continuity Engine conserva la flecha temporal verificable del State OS.

Su misión es:

- establecer el estado génesis;
- registrar transiciones válidas en orden append-only;
- encadenar estados mediante `previous_state_hash → new_state_hash`;
- impedir transiciones huérfanas, replay y bifurcaciones silenciosas;
- permitir reconstrucción temporal del estado;
- alimentar al Palace Observatory con eventos observables.

## II. FRONTERA DE AUTORIDAD

El Continuity Engine **no legisla, no interpreta el Corpus y no decide competencias**.

Acepta únicamente transiciones que hayan sido autorizadas por la capa de decisión competente y que lleguen acompañadas por una prueba de autorización verificable.

La validación semántica de la decisión pertenece al Sovereign Kernel / Decision-Law stack correspondiente.

## III. GÉNESIS

El motor se inicializa una sola vez mediante un `GenesisBlock` derivado de la `GenesisTrustRoot`.

El bloque génesis debe conservar, como mínimo:

- `ceremony_id`;
- `genesis_state_hash`;
- algoritmo criptográfico;
- referencia a la raíz de confianza;
- evidencia de la ceremonia;
- versión del esquema.

La semántica de quién constituye la autoridad génesis proviene del Canon y de Identity & Census, no de una constante escondida en el código.

## IV. TRANSICIÓN CANÓNICA

Cada transición debe contener:

```text
transition_id
parent_state_hash
event_hash
actor_identity
authorization_reference
evidence_reference
schema_version
timestamp
resulting_state_hash
```

El `resulting_state_hash` debe depender determinísticamente del estado anterior y del evento canónico. No se aceptan hashes decorativos basados únicamente en un ID.

## V. REGLAS DE COMMIT

El único commit de una transición válida debe:

1. verificar la autorización proporcionada;
2. verificar que `parent_state_hash == current_head_hash`;
3. comprobar que `transition_id` no haya sido consumido;
4. comprobar que el evento no sea un replay;
5. calcular o verificar el `resulting_state_hash`;
6. añadir el evento al historial append-only;
7. actualizar el head;
8. emitir el evento al Palace Observatory.

Una transición fallida no debe mutar el estado.

## VI. CONCURRENCIA

El motor debe serializar commits sobre un único head lógico o utilizar una estrategia equivalente que preserve la unicidad del siguiente estado.

No se permiten dos hijos válidos del mismo head dentro de una única cadena soberana sin un mecanismo explícito de bifurcación autorizado por el Canon.

## VII. REPLAY Y ORFANDAD

Debe rechazarse toda transición cuyo:

- `transition_id` ya haya sido procesado;
- `parent_state_hash` no coincida con el head actual;
- autorización ya haya sido consumida cuando el contrato así lo requiera;
- evento no corresponda al contexto declarado.

## VIII. RECONSTRUCCIÓN

El motor debe permitir reconstruir el estado de lectura correspondiente a un punto temporal o a un evento específico sin alterar el estado soberano actual.

Esta capacidad alimenta:

- Palace Observatory;
- depuración forense;
- continuidad;
- recuperación;
- pruebas de restauración.

## IX. INMUTABILIDAD

El historial canónico es append-only.

No se permite editar o borrar silenciosamente una transición histórica.

Una corrección se expresa mediante un nuevo evento válido, una reversión o el mecanismo jurídico/técnico que corresponda.

## X. RELACIÓN CON OBSERVATORY

El Palace Observatory recibe una vista de solo lectura del historial y puede comprobar:

`evento → parent state → resulting state → invariantes → evidencia`.

El Observatory no puede escribir en el Continuity Engine.

## XI. SIMULACIÓN Y SOBERANO

El motor debe separar completamente:

- `SIMULATION_ONLY`;
- `SOVEREIGN`.

Una simulación no puede mutar el historial soberano.

Las pruebas de recuperación deben poder operar sobre copias aisladas.

## XII. ESTADOS DE DEPENDENCIA

- `TECHNICAL_IMPLEMENTATION_ALLOWED`: contrato suficiente para implementar.
- `IMPLEMENTATION_DEPENDENCY`: falta integración con Kernel, Ledger, Identity o Observatory.
- `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`: falta una decisión normativa real.

No utilizar `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` para ocultar una carencia puramente técnica.

## XIII. CRITERIO DE ACEPTACIÓN

El módulo será aceptable cuando pueda demostrar, en simulación:

```text
GENESIS
→ transición válida
→ segundo estado
→ replay rechazado
→ transición huérfana rechazada
→ corrupción de hash detectada
→ reconstrucción temporal correcta
→ reinicio desde copia verificada
→ historial sin mutación retrospectiva
```

La misma secuencia de eventos debe producir el mismo head final.

## XIV. REGLA FINAL

> **El Continuity Engine conserva la historia; no decide qué debe ser la historia.**
>
> **El Kernel decide qué transición es legítima.**
>
> **El Palace Observatory verifica que la historia observada coincide con la historia registrada.**
