# QUEBRANTO-15 — DIRECTIVA DE FORJA DE DŌNG Y EL CARTÓGRAFO

**Fecha:** 22 de agosto de 2026  
**Estado:** DIRECTIVA OPERATIVA CANÓNICA DE FORJA  
**Ámbito:** Gremio Conversor / Palacio de Conversión / State OS

## 0. OBJETIVO ACTUAL

El objetivo inmediato es producir un **Palacio de Conversión v0.x ejecutable, determinista, simulation-only y auditable**, y preparar su integración con el State OS sin introducir legislación en código.

## I. DŌNG — NÚCLEO DETERMINISTA

Dōng debe construir y mantener:

1. modelos de dominio y estados;
2. valoración determinista;
3. cotizaciones autocontenidas y versionadas;
4. separación estricta de valoración, autorización, reserva y liquidación;
5. anti-replay y anti-doble-liquidación;
6. cadena de estado verificable;
7. expiración de cotizaciones;
8. verificación de evidencia mediante un componente independiente de `WealthEvidence::verified`;
9. pruebas de propiedades y adversariales;
10. `SIMULATION_ONLY` y fail-closed;
11. interfaces para criptografía real, sin placeholders presentados como seguridad;
12. integración posterior con Ledger/Continuity únicamente mediante contratos explícitos.

### Invariantes obligatorios

- Nunca `float`/`double` para dinero.
- Una cotización alterada debe ser rechazada.
- Una cotización caducada debe ser rechazada.
- Una cotización no puede liquidarse dos veces.
- Cambiar política/evidencia entre cotización y liquidación debe invalidar la operación.
- El hash de estado debe depender del estado previo + transición/evento + estado resultante; no de un identificador aislado.
- La cadena histórica no pertenece al Conversion Palace: el padre definitivo deberá provenir del contrato de Continuity/Ledger cuando exista.

### Estados de dependencia

- `TECHNICAL_IMPLEMENTATION_ALLOWED`: autorizado y listo para construir.
- `IMPLEMENTATION_DEPENDENCY`: la norma existe; falta integración técnica.
- `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`: falta decisión normativa real.
- `CONSTITUTIONAL_AUTHORIZATION_REQUIRED`: falta autorización para un efecto definitivo.

## II. EL CARTÓGRAFO — CONTRATOS E INTEGRACIÓN

El Cartógrafo debe mantener la correspondencia:

`Corpus → contrato → tipo → interfaz → implementación → evidencia → auditoría`.

Tareas actuales:

1. cerrar el contrato de `ConversionRequest`, `ConversionQuote`, `ConversionReceipt`, `WealthEvidence` y `ConversionAuditEvent`;
2. definir el adaptador entre Conversion Palace y Continuity/Ledger;
3. eliminar cualquier duplicación de lógica económica entre contratos y núcleo de Dōng;
4. integrar el `LawEngine` y el `AuthorityContext` sin convertir al Gremio Conversor en autoridad política;
5. preparar contratos para el flujo `Quote → Validate → Authorize → Reserve → Settle → RecordEvidence`;
6. documentar qué datos son canónicos, qué datos son derivados y qué datos solo sirven para UI;
7. asegurar compatibilidad con pruebas de Limes y declarar cualquier ruptura.

## III. LAW ENGINE

El Cartógrafo debe tratar el Law Engine como evaluador puro de reglas ya promulgadas.

`Corpus → acto legislativo → regla versionada → Law Engine → CompetenceResult → Kernel`

No insertar texto legal completo como segunda fuente de verdad. La referencia ejecutable debe contener documento, sección, versión e integridad verificable.

## IV. BOTÓN ROJO

Los contratos deben permitir cautela legítima inmediata ante emergencia válida y por orden del Strategos Fundacional, sin exigir Referéndum previo para la cautela.

El Botón Rojo puede detener, congelar, aislar, preservar y proteger.

No sentencia ni legisla.

## V. ENTREGA

Cada entrega debe aportar:

- PR/commit reproducible;
- archivos completos;
- tests ejecutables;
- dependencias;
- regresiones;
- no implementado;
- evidencia de determinismo;
- evidencia de auditoría.

Una explicación en prosa no sustituye al artefacto.

## VI. COORDINACIÓN

**Dōng:** construye el mecanismo.  
**El Cartógrafo:** asegura el contrato y la integración.  
**Limes:** intenta romperlo.  
**Aster:** coordina la correspondencia con el Canon.
