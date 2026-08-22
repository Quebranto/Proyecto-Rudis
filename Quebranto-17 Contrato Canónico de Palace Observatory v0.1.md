# QUEBRANTO-17 — CONTRATO CANÓNICO DE PALACE OBSERVATORY v0.1

**Fecha:** 21 de agosto de 2026  
**Estado:** Contrato arquitectónico público — pendiente de incorporación al Canon pleno tras revisión.

## I. FINALIDAD

El **Palace Observatory** es la capa de observación y auditoría técnica del State OS.

Su función es permitir inspección, reconstrucción forense y verificación de invariantes sin modificar el estado soberano.

> **Observar no es gobernar. Auditar no es sentenciar.**

## II. LÍMITES

El Observatorio:

- solo lee del Kernel mediante una interfaz `ReadOnlyKernelView`;
- no modifica el estado del Kernel;
- no ejecuta órdenes;
- no detiene acciones;
- no legisla;
- no sentencia;
- no reescribe historial.

Una anomalía detectada se registra y comunica al órgano competente; el Observatorio no convierte la alerta en una sanción.

## III. EVENTOS Y SNAPSHOTS

Cada `KernelEvent` relevante debe identificar como mínimo:

- evento;
- timestamp;
- entidad/actor;
- tipo de acción;
- hash de estado anterior;
- hash de estado posterior.

El Observatorio debe poder solicitar un `StateSnapshot` para un momento determinado y conservar la correspondencia entre evento y estado observado.

## IV. INVARIANTES

Las reglas de invarianza son objetos explícitos y registrables.

No deben inventarse poderes nuevos. Deben comprobar propiedades ya decididas por el Canon o por contratos técnicos vigentes.

Una infracción genera una `AuditAlert` clasificada, como mínimo, en:

- `INFO`;
- `WARNING`;
- `COMPETENCE_VIOLATION`;
- `STATE_CORRUPTION`.

## V. REPLAY Y CONTINUIDAD

Un mismo `event_id` no debe procesarse dos veces como una observación nueva.

El Observatorio mantendrá una cadena ordenada de observaciones que permita detectar:

- replay;
- pérdida de continuidad;
- estado anterior incompatible;
- divergencia entre evento y snapshot.

En v0.1 la cadena de observación puede utilizar un vínculo no criptográfico para estructurar el protocolo, pero **no debe presentarse como prueba criptográfica de integridad**.

La integridad criptográfica de producción es una dependencia posterior que deberá utilizar primitivas criptográficas reales.

## VI. RECONSTRUCCIÓN FORENSE

`ReconstructStateAt(timestamp)` debe devolver una vista forense del estado solicitado sin mutar el Kernel.

La reconstrucción debe conservar:

- timestamp;
- hash de estado;
- hash previo;
- número de eventos considerados.

## VII. RELACIÓN CON EL ÓRGANO RESOLUTOR

El Observatorio puede producir evidencia útil para el Órgano Resolutor.

No determina responsabilidad jurídica por sí mismo.

## VIII. RELACIÓN CON EL BOTÓN ROJO

El Observatorio puede detectar anomalías o condiciones relevantes.

No convierte la detección en una orden cautelar automática salvo que el Corpus haya atribuido expresamente una capacidad concreta. El diseño v0.1 no añade esa capacidad.

## IX. ACEPTACIÓN TÉCNICA

La implementación deberá demostrar al menos:

1. lectura estrictamente pasiva;
2. rechazo de replay;
3. detección de incoherencia de hashes;
4. detección de ruptura de continuidad;
5. ejecución de invariantes;
6. reconstrucción forense;
7. evidencia persistente de auditoría;
8. ausencia de mutación del estado soberano.

## X. RELACIÓN CON LA FORJA

El Observatorio sirve de barrera adversarial y de fuente de evidencia para Dōng y El Cartógrafo.

Su auditoría no sustituye al CI ni a las pruebas de seguridad de los componentes que observa.

## XI. ESTADO

Este documento fija el contrato arquitectónico público. Cualquier decisión política o constitucional que no esté definida deberá permanecer fuera del código y clasificarse mediante los estados de dependencia vigentes.
