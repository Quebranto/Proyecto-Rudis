# QUEBRANTO-18 — MAPA INTEGRADO DE FORJA DEL STATE OS v0.1

## Cadena canónica de construcción

```text
Identity & Census
       ↓
Sovereign Kernel / Decision-Law
       ↓
Economic Core / Conversion Palace
       ↓
Genesis & Continuity Engine
       ↓
Palace Observatory
       ↓
Adversarial Audit
```

## Fronteras

**Identity & Census** identifica entidades y mantiene credenciales jurídicas. No decide política económica.

**Kernel / Decision-Law** decide legitimidad normativa y competencia. No delega esa decisión a módulos de ejecución.

**Conversion Palace** ejecuta políticas económicas inyectadas y produce cotizaciones, liquidaciones simuladas y evidencia. No legisla.

**Genesis & Continuity Engine** conserva la historia aceptada y la encadena. No decide la semántica jurídica de una transición.

**Palace Observatory** observa, verifica invariantes y reconstruye. No ejecuta ni sentencia.

**Limes / auditoría adversarial** intenta falsificar o romper cada frontera.

## Regla de integración

Una operación debe poder reconstruirse mediante:

```text
identidad
→ autorización
→ evidencia
→ política/versionado
→ cotización
→ estado previo
→ transición
→ estado resultante
→ observación
→ auditoría
```

## Simulation / Sovereign

`SIMULATION_ONLY` nunca modifica el estado soberano.

El modo soberano requiere un adaptador de Kernel + Ledger + autorización real. La ausencia de esa integración es una `IMPLEMENTATION_DEPENDENCY`, no una excusa para inventar política.

## Criptografía

Los identificadores/hash de simulación no se presentan como seguridad criptográfica de producción. La producción requerirá proveedores criptográficos reales y contratos de gestión de claves.

## Criterio de cierre v0.1

Los módulos deben poder compilarse y probarse por separado y, progresivamente, atravesar una prueba de integración sin duplicar lógica económica ni autoridad política.
