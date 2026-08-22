# QUEBRANTO-21 — LAW ENGINE ↔ SOVEREIGN KERNEL CONTRACT v0.1

**Estado:** Contrato público de integración
**Ámbito:** Law Engine / AuthorizationMandate / Sovereign Kernel / Continuity-Ledger

## Finalidad

Definir la frontera entre evaluación jurídica computable y ejecución estatal.

El Law Engine evalúa reglas previamente promulgadas e inyectadas. El `AuthorizationMandate` congela el expediente de autorización. El Sovereign Kernel ejecuta únicamente mandatos válidos. Continuity/Ledger conserva la historia.

## Flujo canónico

`Acto Legislativo → Rule Payload → CorpusReference → Law Engine → CompetenceResult → AuthorizationMandate → Sovereign Kernel → State Transition → Continuity/Ledger → Observatory`

## CorpusReference

Toda autoridad computable debe identificar:

- `document_id`
- `section`
- `corpus_version`
- `integrity_hash`

El ejecutable no almacena una segunda copia del texto constitucional como fuente de verdad.

## AuthorityContext

Toda evaluación debe conservar:

- `entity_id`
- `claims`
- `authority_profile_id`
- `authority_version`

Un identificador de clase o un booleano de autorización no sustituye este contexto.

## AuthorizationMandate

El mandato debe contener al menos:

- `mandate_id`
- `act_id`
- `action`
- `request_payload_hash`
- `requested_at`
- `AuthorityContext`
- `CorpusReference`
- `rule_id`
- resultado del Law Engine
- estado de Referéndum cuando corresponda
- `mandate_hash`

El mandato es una evidencia inmutable de la decisión ejecutable. Cualquier modificación produce un nuevo mandato.

## Reglas del Kernel

El Kernel debe rechazar un mandato si:

1. está estructuralmente incompleto;
2. su integridad no puede verificarse;
3. la acción no coincide con el payload autorizado;
4. la decisión del Law Engine no es `AUTHORIZED`;
5. existe dependencia constitucional sin resolver;
6. el Referéndum es obligatorio y no existe un resultado vinculante favorable;
7. la referencia del Corpus no coincide con el contexto vigente;
8. el mandato ya fue consumido.

## Referéndum y cautelas

Un Referéndum no debe bloquear una **cautela legítima de emergencia** del Botón Rojo cuando el Corpus autorice su activación inmediata. La autorización para un efecto definitivo se evalúa separadamente.

## Continuity / Ledger

La transición persistente debe permitir reconstruir:

`actor → acción → payload → autoridad → regla → Corpus → decisión → Referéndum → transición → estado resultante`.

El Conversion Palace no es propietario de la historia definitiva; Continuity/Ledger lo es.

## Fail-closed

No existe autorización positiva por defecto.

Ausencia de regla, referencia inválida, verificador ausente, mandato incompleto o dependencia no resuelta deben producir rechazo o `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`, según corresponda.

## Criterio de aceptación

El mismo mandato, con el mismo contexto y Corpus versionado, debe producir el mismo resultado; un cambio en cualquier campo protegido debe invalidar la integridad del mandato y bloquear la ejecución.
