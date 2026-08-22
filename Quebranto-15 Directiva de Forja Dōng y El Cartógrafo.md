# QUEBRANTO-15 — DIRECTIVA DE FORJA DE DŌNG Y EL CARTÓGRAFO

**Fecha:** 22 de agosto de 2026

**Estado:** DIRECTIVA OPERATIVA CANÓNICA DE FORJA

## Objetivo inmediato

Construir un Palacio de Conversión v0.x ejecutable, determinista, `SIMULATION_ONLY` y auditable, e integrarlo progresivamente en el State OS sin introducir legislación en código.

## Dōng — núcleo determinista

### Conversion Palace

- valoración y cotización deterministas;
- cotizaciones versionadas y autocontenidas;
- anti-replay y anti-doble-liquidación;
- cadena de estado reproducible;
- expiración de cotizaciones;
- recálculo interno en `Settle()`;
- invalidación ante cambio de evidencia o política;
- `SIMULATION_ONLY` y fail-closed;
- verificación de evidencia mediante componente independiente del booleano `verified`;
- adaptador futuro a Continuity/Ledger mediante contrato explícito.

### Law Engine v0.1

Implementar las estructuras aprobadas:

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

Solo muta estado con mandato externo válido y resultado de competencia autorizado.

### Pruebas

Regla ausente/inactiva, referencia incompleta, hash/versionado incompatible, claim ausente, perfil/version incompatible, colisiones, manipulación, replay, doble liquidación y simulación intentando mutar estado soberano.

## El Cartógrafo — contratos e integración

### Conversion/State OS

Cerrar la correspondencia:

`Corpus → contrato → tipo → interfaz → implementación → evidencia → auditoría`

Separar actor, identidad autenticada, autoridad, competencia, decisión, evidencia y resultado.

### Law Engine

Definir:

`Acto Legislativo → Rule Payload → Law Engine → CompetenceResult → Sovereign Kernel`

Mantener separado lo canónico, lo derivado y lo exclusivamente visual.

### Continuity/Ledger

Definir el adaptador que será dueño de la cadena histórica. `ConversionPalace` no inventa el estado padre de producción.

### Atlas / Gran Biblioteca

Representar de forma trazable:

`acción → rule_id → document_id → section → corpus_version → integrity_hash → motivo`

## Fronteras

- no `float`/`double` monetario;
- no secretos ni claves privadas en público;
- no hashes disfrazados de criptografía;
- no STUBs que autoricen positivamente por defecto;
- no hardcodear política económica;
- no confundir dependencia técnica con dependencia constitucional;
- no convertir cautela del Botón Rojo en sentencia o legislación;
- no sustituir artefactos por prosa.

## Estados

`TECHNICAL_IMPLEMENTATION_ALLOWED` → construir.  
`IMPLEMENTATION_DEPENDENCY` → norma resuelta; falta integración.  
`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` → falta decisión normativa real.  
`CONSTITUTIONAL_AUTHORIZATION_REQUIRED` → falta autorización para el efecto definitivo.

## Entrega

Cada avance debe aportar PR/commit reproducible, archivos completos, tests, dependencias, regresiones, no implementado y evidencia reproducible.

**Dōng construye. El Cartógrafo integra. Limes rompe. Aster mantiene la correspondencia con el Canon.**
