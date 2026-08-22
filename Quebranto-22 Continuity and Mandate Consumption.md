# QUEBRANTO-22 — CONTINUITY AND MANDATE CONSUMPTION v0.1

**Estado:** Contrato público de integración  
**Ámbito:** AuthorizationMandate / Conversion Palace / Continuity / Ledger / Observatory

## Finalidad

Garantizar que un `AuthorizationMandate` pueda consumirse una sola vez y que cada transición quede reconstruible mediante una cadena persistente de estados.

## Flujo

`AuthorizationMandate → validación → ejecución → Continuity/Ledger → estado resultante → Observatory`

## Invariantes

1. `mandate_hash` no puede consumirse dos veces.
2. `parent_state_hash` debe existir o ser el Genesis autorizado.
3. El estado resultante debe depender del estado previo y del payload completo de transición.
4. El registro debe conservar `mandate_hash` y `payload_hash`.
5. El Conversion Palace no es propietario de la historia persistente definitiva.
6. Un fallo de Continuity/Ledger impide declarar la transición como liquidada.

## Persistencia

La implementación en memoria es válida únicamente para `SIMULATION_ONLY`. La persistencia de producción pertenece al Continuity/Ledger y deberá ser durable, auditable y resistente a replay.

## Mandato e integridad

El mandato debe conservarse como expediente completo, incluyendo actor, acción, payload, autoridad, CorpusReference, regla, decisión y estado de Referéndum cuando corresponda.

La integridad del mandato se verifica mediante una serialización canónica y un proveedor criptográfico real. Un hash de simulación no se considera seguridad de producción.

## Criterio de aceptación

Un segundo consumo del mismo mandato, una transición huérfana o una manipulación de cualquier campo protegido deben producir rechazo verificable y no generar una mutación soberana.
