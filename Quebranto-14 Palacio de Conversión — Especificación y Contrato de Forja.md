# QUEBRANTO-14 — PALACIO DE CONVERSIÓN

**Fecha:** 21 de agosto de 2026  
**Estado:** ESPECIFICACIÓN INSTITUCIONAL Y TÉCNICA DE FORJA  
**Órgano:** Gremio Conversor de Riqueza  
**Auditoría:** Palacio de Tormentas  
**Forjadores:** Dōng + El Cartógrafo, bajo coordinación de Aster

## I. FINALIDAD

El **Palacio de Conversión** es la infraestructura operativa del Gremio Conversor que traduce riqueza demostrable en valor liquidable dentro y fuera de Rudis.

Su cadena principal es:

> **evidencia → valoración → cotización → costes → autorización → liquidación → registro → auditoría**

Y su retorno:

> **fiat → cotización → RU → liquidación interna**

El Palacio no es legislador ni juez. Ejecuta políticas vigentes y devuelve dependencias cuando falta una decisión normativa.

## II. RELACIÓN CON EL GREMIO CONVERSOR

El Gremio Conversor es la función/órgano económico.

El Palacio de Conversión es su **infraestructura operativa y visible dentro del State OS**.

El Gremio determina y supervisa la política conforme al Corpus y a la Asamblea; el Palacio calcula, registra, liquida y expone la evidencia.

## III. ROLES

### Dōng

Responsable técnico de:

- estado monetario;
- balances y reservas;
- ledger de operaciones;
- cálculos deterministas;
- validación de conversiones;
- API interna del núcleo.

### El Cartógrafo

Responsable técnico de:

- contratos de integración;
- State OS / Economic Core;
- Guild Runtime;
- Atlas Soberano;
- instrumentación del Palacio;
- integración de pruebas.

### Aster

Responsable de dirección de forja y correspondencia con el Canon.

### Palacio de Tormentas

Responsable de auditoría independiente de:

- evidencia;
- trazabilidad;
- determinismo;
- reservas;
- integridad de estados;
- y ausencia de autoridad técnica inventada.

## IV. OBJETOS DEL DOMINIO

El núcleo utilizará, como mínimo:

- `WealthEvidence`
- `ConversionPolicy`
- `ConversionRequest`
- `ConversionQuote`
- `ConversionReceipt`
- `RUAsset`
- `TreasuryState`
- `SovereignFundLedgerEntry`
- `ConversionAuditEvent`

## V. POLÍTICAS

No se hardcodearán:

- tipo RU/fiat;
- comisión;
- contribución de actividad;
- interés evolutivo;
- reservas;
- emisión;
- límites de crédito;
- reglas fiscales.

Toda política económica deberá estar versionada.

El código debe poder demostrar **qué versión de política produjo una cotización**.

## VI. ORO DIGITAL

RU se diseña como activo monetario digital con propiedades inspiradas en el oro:

- escasez controlada;
- autenticidad verificable;
- resistencia a falsificación;
- procedencia;
- transferencia verificable;
- fraccionamiento;
- y capacidad de asociar/encapsular mensajes o metadatos verificables.

La información asociada no altera silenciosamente el valor monetario.

## VII. ENTRADA / SALIDA

El Palacio soportará:

- visitantes;
- habitantes;
- ciudadanos;
- operaciones comerciales;
- remuneración de trabajo;
- productos/servicios;
- activos digitales;
- inversión;
- entrada;
- salida;
- retorno.

Los costes se mostrarán separadamente:

1. importe bruto;
2. referencia;
3. coste de gestión;
4. contribución de actividad;
5. interés/coste evolutivo;
6. ajustes autorizados;
7. importe neto.

## VIII. SIMULACIÓN

La primera implementación solo podrá **simular** liquidaciones.

Toda simulación deberá conservar:

- `simulation_id`;
- `parent_state_hash`;
- versión de política;
- estado de origen;
- ledger de simulación;
- evidencia reproducible.

La simulación no puede modificar el estado soberano.

## IX. LIQUIDACIÓN SOBERANA

El backend de liquidación soberana queda deliberadamente desacoplado.

No se conectarán cuentas bancarias reales, proveedores financieros reales ni dinero real hasta que:

- el modelo de custodia esté definido;
- la criptografía haya sido auditada;
- la política de emisión/reservas sea ejecutable;
- el Palace Observatory pueda verificar cada operación;
- y la transición a producción haya sido autorizada.

## X. FONDO SOBERANO

Los ingresos netos del Palacio que correspondan al ecosistema podrán alimentar el Fondo Soberano según la política vigente.

Cada movimiento deberá generar evidencia específica y poder reconstruirse desde el Ledger.

## XI. CRITERIOS DE ACEPTACIÓN

La primera versión deberá demostrar:

```text
riqueza demostrable
→ evidencia válida
→ valoración
→ cotización
→ costes separados
→ estado de autorización
→ liquidación simulada
→ recibo
→ evidencia
→ auditoría
```

Y deberá demostrar que un mismo input + misma política + mismo estado producen la misma cotización.

## XII. ESTADOS DE FORJA

- `TECHNICAL_IMPLEMENTATION_ALLOWED`
- `IMPLEMENTATION_DEPENDENCY`
- `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`
- `CONSTITUTIONAL_AUTHORIZATION_REQUIRED`

La ausencia de política no se convierte en un cero silencioso: se devuelve un estado explícito.

## XIII. REGLA FINAL

> **El Palacio de Conversión no decide cuánto vale el mundo por voluntad propia.**
>
> **Hace explícita, reproducible y auditable la conversión que la política vigente autoriza.**
>
> **El dinero puede moverse. La evidencia no puede desaparecer.**
