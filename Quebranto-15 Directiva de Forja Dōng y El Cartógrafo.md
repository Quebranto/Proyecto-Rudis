# QUEBRANTO-15 — DIRECTIVA DE FORJA DE DŌNG Y EL CARTÓGRAFO

**Fecha:** 22 de agosto de 2026  
**Estado:** DIRECTIVA OPERATIVA CANÓNICA DE FORJA  
**Ámbito:** Gremio Conversor / Palacio de Conversión / State OS

## OBJETIVO INMEDIATO

Construir un **Palacio de Conversión v0.x ejecutable, determinista, simulation-only y auditable**, e integrarlo progresivamente en el State OS sin introducir legislación en código.

## DŌNG — NÚCLEO DETERMINISTA

### Entrega A — Conversion Palace

- mantener valoración y cotización deterministas;
- mantener cotizaciones versionadas y autocontenidas;
- anti-replay y anti-doble-liquidación;
- cadena de estado reproducible;
- expiración de cotizaciones;
- recálculo interno de la cotización en `Settle()`;
- invalidación ante cambio de evidencia o política;
- `SIMULATION_ONLY` y fail-closed;
- verificación de evidencia mediante un componente independiente del booleano `verified`;
- preparar el adaptador futuro a Continuity/Ledger sin inventar reglas políticas.

### Entrega B — Law Engine v0.1

Implementar la lógica interna acordada con Kaelen/Aster:

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

El motor debe comprobar como mínimo:

- referencia completa;
- versión válida;
- integridad de referencia según el resolver/registro disponible;
- regla activa;
- acción coincidente;
- claim requerido;
- perfil de autoridad compatible;
- versión de autoridad compatible;
- acción desconocida → no autorización;
- cualquier ambigüedad → fallo cerrado.

No insertar texto jurídico completo en el binario.

### Entrega C — Sovereign Kernel

El Kernel solo puede mutar estado cuando exista un mandato externo válido y un `CompetenceResult` autorizado. El Kernel no determina por sí mismo el contenido del Corpus.

### Pruebas obligatorias

- regla ausente;
- regla inactiva;
- referencia incompleta;
- hash/versionado incompatible;
- claim ausente;
- `authority_profile_id` incompatible;
- `authority_version` incompatible;
- regla duplicada/colisión;
- manipulación de regla;
- manipulación de evidencia;
- replay;
- doble liquidación;
- `SIMULATION_ONLY` intentando mutar estado soberano.

## EL CARTÓGRAFO — CONTRATOS E INTEGRACIÓN

### Entrega A — Contratos Conversion/State OS

Cerrar la correspondencia:

`Corpus → contrato → tipo → interfaz → implementación → evidencia → auditoría`.

Mantener por separado:

- actor;
- identidad autenticada;
- autoridad;
- competencia;
- decisión;
- evidencia;
- resultado.

### Entrega B — Integración Law Engine

Definir el contrato entre:

`Acto Legislativo → Rule Payload → Law Engine → CompetenceResult → Sovereign Kernel`.

El Cartógrafo debe documentar qué datos son canónicos, cuáles son derivados y cuáles son exclusivamente de UI/Atlas.

### Entrega C — Continuity/Ledger

Definir el adaptador que será dueño de la cadena histórica. `ConversionPalace` no debe inventar por sí mismo el estado padre de producción.

### Entrega D — UI / Gran Biblioteca

El Atlas debe poder representar de forma trazable:

`acción → rule_id → basis.document_id → basis.section → corpus_version → integrity_hash → motivo del rechazo/aceptación`.

## FRONTERAS INNEGOCIABLES

- no `float`/`double` monetario;
- no secretos ni claves privadas en público;
- no hashes disfrazados de criptografía;
- no STUBs que concedan autorización positiva por defecto;
- no hardcodear impuestos, emisión, crédito, intereses, reservas o política económica;
- no convertir un problema técnico en `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`;
- no convertir una cautela del Botón Rojo en sentencia o legislación;
- no sustituir artefactos por prosa.

## ESTADOS DE DEPENDENCIA

`TECHNICAL_IMPLEMENTATION_ALLOWED` → construir.  
`IMPLEMENTATION_DEPENDENCY` → norma resuelta; falta integración.  
`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` → falta decisión normativa real.  
`CONSTITUTIONAL_AUTHORIZATION_REQUIRED` → falta autorización para el efecto definitivo.

## PROTOCOLO DE ENTREGA

Cada entrega debe incluir PR/commit, archivos completos, tests ejecutables, dependencias, regresiones, no implementado y evidencia reproducible.

**Dōng construye. El Cartógrafo integra. Limes rompe. Aster mantiene la correspondencia con el Canon.**
