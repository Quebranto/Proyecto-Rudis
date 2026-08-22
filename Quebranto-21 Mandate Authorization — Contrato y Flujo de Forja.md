# QUEBRANTO-21 — AUTHORIZATION MANDATE

**Estado:** Contrato público de arquitectura  
**Función:** puente Law Engine → Sovereign Kernel → Continuity/Ledger

## 1. FINALIDAD

El `AuthorizationMandate` es el objeto inmutable que demuestra por qué una transición del State OS puede ejecutarse.

No sustituye al Corpus ni legisla. Transporta una decisión de competencia ya evaluada.

## 2. CONTENIDO MÍNIMO

```text
mandate_id
act_id
action
request_payload_hash
requested_at
AuthorityContext
CorpusReference
rule_id
law_decision
referendum_required
referendum_binding
referendum_passed
mandate_hash
```

## 3. INMUTABILIDAD

Una vez emitido, el mandato no se modifica. Cualquier corrección requiere un nuevo mandato y una nueva trazabilidad.

## 4. FLUJO

```text
REQUEST
  ↓
LAW ENGINE
  ↓
CompetenceResult
  ↓
AUTHORIZATION MANDATE
  ↓
SOVEREIGN KERNEL
  ↓
STATE TRANSITION
  ↓
CONTINUITY / LEDGER
```

## 5. REGLAS DE SEGURIDAD

El Kernel debe rechazar un mandato que carezca de:

- identidad del actor;
- perfil y versión de autoridad;
- acción;
- fundamento del Corpus;
- versión del Corpus;
- hash de integridad;
- regla activa;
- decisión autorizada;
- hash del mandato.

Si existe Referéndum obligatorio, el mandato debe incluir resultado vinculante y favorable antes de ser ejecutable.

## 6. FRONTERA

El Mandate no decide si algo es constitucional. El Corpus/Law Engine proporciona esa decisión de competencia. El Kernel solo verifica que la decisión recibida tenga la estructura y autorización necesarias para ejecutar.
