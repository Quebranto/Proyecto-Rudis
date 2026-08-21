# QUEBRANTO-14 — PALACIO DE CONVERSIÓN

**Fecha:** 21 de agosto de 2026  
**Estado:** ESPECIFICACIÓN PÚBLICA DE FORJA  
**Implementación:** repositorio privado `Quebranto/tt`  
**Órgano:** Gremio Conversor de Riqueza  
**Auditoría:** Palacio de Tormentas  
**Forjadores:** Dōng + El Cartógrafo, bajo coordinación de Aster

## I. FINALIDAD

El **Palacio de Conversión** es la infraestructura operativa del Gremio Conversor que traduce riqueza demostrable en valor liquidable dentro y fuera de Rudis.

Cadena principal:

> **evidencia → valoración → cotización → costes → autorización → liquidación → registro → auditoría**

Y su retorno:

> **fiat → cotización → RU → liquidación interna**

El Palacio no legisla ni juzga. Ejecuta políticas vigentes y devuelve dependencias cuando falta una decisión normativa.

## II. RELACIÓN CON EL GREMIO CONVERSOR

El Gremio Conversor es la función/órgano económico.

El Palacio de Conversión es su infraestructura operativa y visible dentro del State OS.

## III. IMPLEMENTACIÓN

El código del Palacio de Conversión se conserva en el repositorio privado del ecosistema.

El repositorio público mantiene únicamente la especificación necesaria para comprender:

- finalidad;
- contratos conceptuales;
- fronteras de autoridad;
- estados de implementación;
- criterios de aceptación;
- e integración con el State OS.

Los detalles operativos de seguridad, custodia, producción y mecanismos antifraude no se documentan aquí.

## IV. OBJETOS DEL DOMINIO

- `WealthEvidence`
- `ConversionPolicy`
- `ConversionRequest`
- `ConversionQuote`
- `ConversionReceipt`
- `RUAsset`
- `TreasuryState`
- `ConversionAuditEvent`

Las definiciones ejecutables y sus implementaciones viven en el repositorio privado.

## V. POLÍTICAS

No se hardcodean políticamente en el código:

- tipo RU/fiat;
- comisiones;
- contribución de actividad;
- coste/interés evolutivo;
- reservas;
- emisión;
- crédito;
- reglas fiscales.

Toda política económica debe estar versionada.

## VI. RU / ORO DIGITAL

RU se diseña conceptualmente como activo monetario digital inspirado en propiedades del oro:

- escasez controlada;
- autenticidad verificable;
- resistencia a falsificación;
- procedencia;
- transferencia verificable;
- fraccionamiento;
- y posibilidad de asociar información verificable.

La especificación pública **no expone los mecanismos internos de seguridad o custodia**.

## VII. SIMULACIÓN

La primera implementación es `SIMULATION_ONLY`.

La simulación no modifica el estado soberano.

## VIII. PRODUCCIÓN

No se conectarán dinero real, bancos reales, custodias de producción ni proveedores financieros externos hasta completar las auditorías y autorizaciones pertinentes.

## IX. CRITERIOS DE ACEPTACIÓN

La primera versión debe demostrar:

```text
riqueza demostrable
→ evidencia válida
→ valoración
→ cotización
→ costes separados
→ autorización
→ liquidación simulada
→ recibo
→ evidencia
→ auditoría
```

La misma entrada, política y evidencia debe producir una cotización determinista.

## X. ESTADOS DE FORJA

- `TECHNICAL_IMPLEMENTATION_ALLOWED`
- `IMPLEMENTATION_DEPENDENCY`
- `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`
- `CONSTITUTIONAL_AUTHORIZATION_REQUIRED`

## XI. REGLA FINAL

> **El Palacio de Conversión no decide cuánto vale el mundo por voluntad propia.**
>
> **Hace explícita, reproducible y auditable la conversión que la política vigente autoriza.**
>
> **La implementación pertenece al repositorio privado; el contrato pertenece al Corpus público.**
