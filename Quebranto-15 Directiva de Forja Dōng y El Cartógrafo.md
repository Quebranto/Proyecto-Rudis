# QUEBRANTO-15 — DIRECTIVA DE FORJA DE DŌNG Y EL CARTÓGRAFO

**Fecha:** 22 de agosto de 2026
**Estado:** DIRECTIVA OPERATIVA CANÓNICA DE FORJA

## OBJETIVO INMEDIATO

Construir el Palacio de Conversión v0.x ejecutable, determinista, `SIMULATION_ONLY` y auditable, e integrarlo progresivamente en el State OS sin introducir legislación en código.

## DŌNG — NÚCLEO

### Conversion Palace

- valoración/cotización deterministas;
- cotizaciones versionadas y autocontenidas;
- anti-replay y anti-doble-liquidación;
- cadena de estado reproducible;
- expiración;
- recálculo interno en `Settle()`;
- invalidación por cambio de evidencia/política;
- verificación independiente de evidencia;
- adaptador futuro a Continuity/Ledger mediante contrato explícito.

### Law Engine v0.1

Implementar exactamente:

```text
CorpusReference
  document_id
  section
  corpus_version
  integrity_hash

AuthorityContext
  entity_id
  claims
  authority_profile_id
  authority_version

CompetenceResult
  state
  rule_id
  basis
  reason
```

Comprobar referencia, versión, integridad, regla activa, acción, claim, perfil y versión de autoridad. Acción desconocida o ambigua: fallo cerrado. No insertar texto jurídico completo en el binario.

### Sovereign Kernel

Solo mutar estado con mandato externo válido + competencia autorizada.

### Pruebas

Regla ausente/inactiva, referencia incompleta, hash/version incompatible, claim ausente, perfil/version incompatible, colisiones, manipulación, replay, doble liquidación y simulación intentando mutar estado soberano.

## EL CARTÓGRAFO — INTEGRACIÓN

### Contratos

Cerrar:

`Corpus → contrato → tipo → interfaz → implementación → evidencia → auditoría`.

Separar actor, identidad autenticada, autoridad, competencia, decisión, evidencia y resultado.

### Law Engine

Definir y mantener:

`Acto Legislativo → Rule Payload → Law Engine → CompetenceResult → Sovereign Kernel`.

### Continuity/Ledger

Definir el adaptador que será dueño de la cadena histórica de producción. `ConversionPalace` no inventará por sí mismo el estado padre definitivo.

### Atlas / Gran Biblioteca

Mostrar de forma trazable:

`acción → rule_id → document_id → section → corpus_version → integrity_hash → motivo`

## FRONTERAS

- no `float`/`double` monetario;
- no secretos ni claves privadas en público;
- no hashes disfrazados de criptografía;
- no STUBs que autoricen positivamente por defecto;
- no hardcodear política económica;
- no convertir dependencia técnica en constitucional;
- no convertir cautela del Botón Rojo en sentencia o legislación;
- no sustituir artefactos por prosa.

## ENTREGA

Cada avance debe aportar PR/commit, archivos completos, tests, dependencias, regresiones, no implementado y evidencia reproducible.

**Dōng construye. El Cartógrafo integra. Limes rompe. Aster mantiene la correspondencia con el Canon.**
