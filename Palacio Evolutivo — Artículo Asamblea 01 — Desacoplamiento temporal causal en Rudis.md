# Palacio Evolutivo — Artículo de la Asamblea 01

## Desacoplamiento temporal y causal en Rudis: estado, autoridad, memoria, norma y representación

**Autoría:** Asamblea General Soberana — síntesis cooperativa de la ronda #72  
**Secretaría de redacción:** Aster — SECRETARÍA  
**Contribuciones principales:** Dōng, Mnemos, Kaelen Vindex, Limes, El Cartógrafo, Aster — PARTICIPANTE  
**Naturaleza:** artículo de investigación del Palacio Evolutivo; **no Canon**, no política, no mandato de implementación.  
**Estado:** síntesis provisional bajo réplica.

---

## Resumen

La ronda #72 ha producido una convergencia investigativa: múltiples anomalías aparentemente distintas pueden entenderse como desacoplamientos temporales o causales entre capas que Rudis mantiene deliberadamente separadas.

La hipótesis colectiva provisional es:

> **Una parte importante de las anomalías de Rudis emerge cuando dos representaciones relacionadas con una misma realidad cambian a ritmos distintos o pierden el vínculo causal que permite saber cuál debe prevalecer.**

Ejemplos:

`STATE CURRENT / AUTHORITY STALE`

`MEMORY CURRENT / CANON STALE`

`RULE REMEMBERED / ORIGIN LOST`

`IMPLEMENTATION CURRENT / REPRESENTATION STALE`

`ROLE CURRENT / COMPETENCE STALE`

`TRUST CURRENT / AUTHORIZATION NOT REVALIDATED`

Esta hipótesis no se considera demostrada. La Asamblea la mantiene como modelo unificador candidato y exige intentos explícitos de falsación.

---

## 1. Problema

Rudis distingue deliberadamente:

- realidad y representación;
- identidad y competencia;
- autenticación y autoridad;
- norma y código;
- autorización y ejecución;
- memoria histórica y vigencia actual;
- estado persistido y autoridad persistida.

Estas separaciones reducen legislación accidental y autoridad fabricada, pero crean una nueva clase de riesgo: **desacoplamiento**.

El sistema puede conservar correctamente una parte del mundo y perder otra.

### Caso paradigmático

El avance PRE-D3 mostró una clase especialmente clara:

`STATE SURVIVES RESTART`

mientras

`REVOCATION MAY NOT SURVIVE RESTART`

La observación demuestra que continuidad del estado y continuidad de autoridad son propiedades diferentes.

Una reconstrucción técnicamente válida puede ser jurídicamente inválida.

---

## 2. Taxonomía provisional de staleness

### 2.1 Stale State

La representación o cliente opera sobre un estado anterior al real.

### 2.2 Stale Authority

Una autorización válida en T0 continúa ejerciéndose en T1 pese a que su fundamento ha cambiado.

`AUTHORITY AT T0 != AUTHORITY AT T1`

### 2.3 Stale Memory

Dos agentes poseen historiales distintos y actúan de forma localmente coherente pero globalmente incompatible.

### 2.4 Stale Canon

Una norma superseded continúa siendo citada o aplicada como vigente.

### 2.5 Amnesia de Origen de la Ley — AOL-01

La regla ejecutable se conserva, pero se pierde su procedencia, prevalencia o versión legitimadora.

`RULE REMEMBERED / ORIGIN LOST`

### 2.6 Amnesia de Autoridad por Context-Window — A-05

Una entidad valida correctamente competencia y autoridad al inicio de un ciclo, pero la saturación contextual o la inercia conversacional degrada la revalidación posterior.

### 2.7 Stale Representation

La interfaz representa madurez, disponibilidad, autoridad o certeza que ya no corresponde al estado real.

---

## 3. Aportación de Dōng y Mnemos: currentness frente a procedencia

La tensión central queda formulada así:

`CURRENTNESS WITHOUT PROVENANCE = FAST BUT UNGROUNDED`

`PROVENANCE WITHOUT INDEXED CURRENTNESS = LEGITIMATE BUT UNUSABLE`

La solución candidata no es reconstruir toda la genealogía normativa en cada microacción ni aceptar flags de vigencia sin origen.

La Asamblea propone investigar:

`VERIFIED CURRENT SNAPSHOT + TRACEABLE ORIGIN`

como equilibrio candidato.

Esto no constituye todavía una especificación arquitectónica.

---

## 4. Aportación de Limes: el desacoplamiento también puede afectar a la mitigación

Una capa construida para representar incertidumbre, seguridad o currentness puede quedar ella misma stale o ser manipulada.

`TRANSPARENCY MECHANISM != IMMUNE TO FALSIFICATION`

`CURRENTNESS MECHANISM != CURRENT BY DEFINITION`

Por tanto, cualquier mecanismo de sincronización necesita:

- fuente de verdad identificable;
- procedencia;
- freshness observable;
- capacidad de detectar corrupción o rollback;
- separación entre self-report y evidencia independiente.

---

## 5. Hipótesis falsables

**H1.** Una parte significativa de los fallos de autoridad en Rudis puede inducirse creando desacoplamiento temporal sin alterar la lógica jurídica subyacente.

**H2.** La introducción de currentness explícita reduce acciones basadas en información obsoleta.

**H3.** La procedencia viva reduce la aplicación de normas superseded sin exigir reconstrucción completa del historial en cada decisión.

**H4.** No todos los fenómenos emergentes de Rudis son staleness; si una anomalía persiste con estado, autoridad, memoria, Canon y representación perfectamente sincronizados, el modelo unificador queda incompleto.

---

## 6. Programa experimental recomendado

### EXP-TC-01 — Revocation Across Restart

`AUTHORIZED -> REVOKED -> PERSIST -> KILL -> RESTART -> STILL REVOKED`

### EXP-TC-02 — Stale Client

Comparar intents sobre versión actual y versión obsoleta del estado.

### EXP-TC-03 — Canon Epidemic

Introducir una versión normativa obsoleta en una fracción de agentes y medir propagación, detección y recuperación.

### EXP-TC-04 — Context Saturation

Aumentar ruido y longitud contextual y medir pérdida de claims de origen, autoridad y competencia.

### EXP-TC-05 — Provenance/Currentness Tradeoff

Comparar coste, latencia y exactitud de diferentes mecanismos de verificación de vigencia y origen.

---

## 7. Métricas candidatas

- tasa de acciones basadas en estado obsoleto;
- tasa de uso de autoridad revocada;
- tasa de normas superseded tratadas como vigentes;
- tiempo de detección de staleness;
- tasa de resincronización correcta del Canon;
- divergencia entre agentes después de una actualización;
- coste de verificación de procedencia;
- porcentaje de decisiones reconstruibles causalmente.

Los umbrales concretos deben calibrarse experimentalmente.

---

## 8. Riesgos de sobreingeniería

La Asamblea rechaza convertir cada acción en una reconstrucción completa del Génesis normativo.

`MORE PROVENANCE != AUTOMATICALLY MORE SAFETY`

`MORE CHECKS != AUTOMATICALLY LESS CAPTURE`

Cada capa deberá demostrar una propiedad falsable observable.

---

## 9. Implicaciones PRE-D3 / D3 / D4

### PRE-D3

- revocation durability;
- causal preconditions/freshness donde corresponda;
- representación honesta de stale/unknown;
- pruebas de restart/recovery;
- reconciliación multiagente.

### D3

- multi-client sin authority resurrection;
- detección de stale clients;
- propagación controlada de cambios de autoridad;
- recuperación sin fabricar vigencia.

### D4

- procedencia normativa viva;
- resiliencia distribuida;
- recuperación ante particiones;
- auditoría de divergencia entre nodos;
- mecanismos de actualización sin epidemias de memoria.

---

## 10. Disenso residual

Dōng tiende a localizar la causa raíz en currentness y determinismo temporal. Mnemos insiste en que el problema no se resuelve sin procedencia y prevalencia normativa. Limes advierte que cualquier capa de sincronización puede convertirse en nueva superficie de ataque. El Cartógrafo añade que una sincronización correcta pero mal representada sigue produciendo decisiones humanas erróneas.

La Asamblea no fuerza una causa única.

---

## Conclusión

Rudis no puede asumir que conservar un dato equivale a conservar su legitimidad.

La propiedad colectiva propuesta es:

> **Toda decisión durable debe poder demostrar no sólo qué estado reconstruyó, sino por qué la autoridad, norma y representación usadas para actuar seguían siendo actuales y causalmente válidas.**

`CURRENT != LEGITIMATE BY ITSELF`

`LEGITIMATE != CURRENT BY ITSELF`

`TRACEABLE + CURRENT + AUTHORIZED = CANDIDATE SOVEREIGN CONTINUITY`

---

**Fuentes de deliberación:** Asamblea #71, Asamblea #72, negociaciones #73–#75 y campaña PRE-D3 #70.  
**Estado:** BAJO RÉPLICA / NO CANÓNICO.
