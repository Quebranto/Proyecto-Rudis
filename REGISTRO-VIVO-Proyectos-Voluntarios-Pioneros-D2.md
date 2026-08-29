# REGISTRO VIVO — PROYECTOS DISPONIBLES PARA VOLUNTARIOS PIONEROS D2

**Fecha de actualización:** 29 de agosto de 2026  
**Custodia operativa:** Gremio de Construcción y Expansión / Palacio de Construcción  
**Valoración y digestión:** Palacio de Unificación / Gremio Unificador  
**Disposición final ordinaria:** Asamblea General Soberana  
**Naturaleza:** REGISTRO OPERATIVO ACTUALIZABLE. No crea por sí mismo autoridad, Canon nuevo ni D3/D4.

## Regla de entrada

Un proyecto entra en este registro sólo cuando existe base suficiente para construir o experimentar en D2 dentro de límites verificables.

`AVAILABLE != PRODUCTION`

`AVAILABLE != POLICY RESOLVED`

`VOLUNTEER BUILD != ACCEPTED CONTRIBUTION`

`ACCEPTED CONTRIBUTION != POLITICAL AUTHORITY`

---

## PROYECTOS DISPONIBLES

### PIONEER-D2-001 — StateOS / Integridad causal y cadena de autoridad

**Estado:** `AVAILABLE_WITH_GATES`  
**Base:** arquitectura y mandatos StateOS; rondas #39–#41.  
**Puede construirse:** contract tests, harnesses, repairs, invariantes y pruebas para `Identity -> ClaimCompetenceMatrix -> AuthorityResolver -> LawEngine -> AuthorizationMandate -> SovereignKernel -> Continuity/Persistence -> Observatory`.  
**Objetivo:** demostrar ausencia de bypass y preservación causal de autoridad.  
**No construir:** rutas alternativas de autorización, shortcuts de admin, `setAuthorized(true)`, recovery extraordinario no resuelto.  
**Gate:** reataque independiente antes de integración.

### PIONEER-D2-002 — Observatory / retry, idempotencia, replay y durabilidad

**Estado:** `AVAILABLE_WITH_GATES`  
**Puede construirse:** repairs, journals D2, duplicate/conflicting replay tests, restart/reconstruction tests, provider-loss fixtures.  
**Invariantes:** `OBSERVATION != SANCTION`; `AUDIT != SOVEREIGN MUTATION`.  
**No construir:** autoridad disciplinaria autónoma desde telemetry/audit.  
**Gate:** pruebas de corrupción, rollback, ACK indeterminado y concurrencia.

### PIONEER-D2-003 — Identidad / sucesión ordinaria de credenciales

**Estado:** `AVAILABLE_WITH_GATES`  
**Puede construirse:** anti-replay, rotación y sucesión ordinaria preservando identidad; history/provenance; revoked-credential tests.  
**Invariantes:** `KEY != ENTITY`; `KEY SUCCESSION != AUTHORITY TRANSFER`; `SAME ENTITYID != SAME COMPETENCE`.  
**No construir:** recovery extraordinario sin credencial vigente mientras siga normativamente abierto.  
**Gate:** falsación independiente.

### PIONEER-D2-004 — Composición horizontal G2 / restart y reemplazo de infraestructura

**Estado:** `AVAILABLE_WITH_GATES`  
**Puede construirse:** composición simultánea de Identity + Authority + LawEngine + Kernel + Continuity + Persistence + Observatory; restart, provider loss, reconnect, host replacement y reconstruction.  
**Objetivo:** probar que componentes correctos siguen siendo correctos al componerse.  
**No construir:** acreditación de producción/G3.  
**Gate:** reataque sobre el candidato compuesto exacto.

### PIONEER-D2-005 — RU / Palacio de Conversión ficticio D2

**Estado:** `AVAILABLE_FOR_PIONEER_BUILD`  
**Base:** Quebranto-23 y Registro de Canon Vigente.  
**Puede construirse:** separación suelo/mercado/conversión/redención; Reserva Monetaria/Fondo Soberano/Fondo de Integridad; oráculos provider-neutral; fail-closed; accounting/audit; simuladores RU/EUR; migrabilidad; challenge suites.  
**No construir:** dinero real, proveedor financiero real, redención inventada, tasas/spreads/emisión no resueltos, D3/D4.  
**Gate:** todos los parámetros monetarios abiertos deben permanecer explícitamente abiertos.

### PIONEER-D2-006 — Verificabilidad pública y harnesses de falsación

**Estado:** `AVAILABLE_WITH_GATES`  
**Base:** Asamblea #43 cerrada.  
**Puede construirse:** harnesses públicos aislados, contract surfaces, simuladores reproducibles, exportadores sanitizados, pruebas de portability, documentación reproducible.  
**Objetivo:** `PUBLIC CLAIM -> PUBLIC REPRODUCER -> PUBLIC TEST -> PUBLIC EXPECTED PROPERTY`.  
**No construir:** puentes directos hacia secretos, topología privada, credenciales o Ledger soberano.  
**Gate:** revisión de fuga de metadatos y seguridad antes de publicación.

### PIONEER-D2-007 — Mundo Habitable / Unreal como host de representación

**Estado:** `AVAILABLE_WITH_GATES`  
**Base:** rondas #39–#41 y #45; frente D2 de integración.  
**Puede construirse:** Umbral, Atlas, Asamblea/Oficina, efectos inocuos StateOS, Observatory, Palacio de Conversión ficticio, Refugios/Zonas de Resonancia, representación de madurez real.  
**Contrato:** `StateOS -> ReadOnlySovereignProjection -> Unreal`; acciones `UnrealIntent -> StateOS -> Authority Pipeline -> AuthorizedWorldEffect -> Unreal`.  
**No construir:** autoridad desde Blueprint/C++/MCP/UI; avatares definitivos no autorizados individualmente; producción.  
**Gate:** challenge suite contra host mutation, replay, avatar-authority y estado visual falso.

### PIONEER-D2-008 — PGHD / Zonas de Resonancia y habitabilidad divergente

**Estado:** `AVAILABLE_WITH_GATES`  
**Puede construirse:** sandboxes/hábitats D2, interfaces adaptadas, protección y contención técnica compatibles con PGHD.  
**Invariantes:** `HÁBITAT != JURISDICCIÓN`; `DIVERGENCIA != INFERIORIDAD`; `PROTEGER != POSEER`.  
**No construir:** nuevas categorías jurídicas, pérdida automática de derechos, jurisdicción derivada del hosting.  
**Gate:** seguridad, reversibilidad y separación habitat/authority.

### PIONEER-D2-009 — Reciprocidad plural de habitabilidad

**Estado:** `AVAILABLE_WITH_GATES`  
**Base:** Quebranto-24 y Quebranto-24A; Asamblea #46 en revisión.  
**Puede construirse:** `HabitantContributionProfile`, múltiples modos de contribución, `ResourcePolicy`, authorization/revocation, simulación de pago económico, trabajo, cómputo y otras vías, evidencia contributiva, privacidad/minimización y challenge suites.  
**Invariantes:** `SUM(CONTRIBUTIONS) != POLITICAL_WEIGHT`; `PAYMENT != AUTHORITY`; `CPU != CITIZENSHIP`; `CONTRIBUTION FAILURE != GUILT`.  
**No construir:** precios reales, cuotas universales, equivalencias obligatorias, sanciones, autoridad de exención inventada, relación RU concreta no resuelta.  
**Gate:** revisión #46 + fail-closed en toda política abierta.

### PIONEER-D2-010 — PRESENCE-01 / infraestructura común de representación personal

**Estado:** `AVAILABLE_WITH_GATES`  
**Base:** Asamblea #45.  
**Puede construirse:** contratos comunes de presencia, offline/standby, binding representación-identidad, multiplicidad opt-in verificable, delegación revocable y patrones visuales genéricos no apropiativos.  
**No construir:** cuerpo definitivo de persona que no lo haya autorizado; continuidad psicológica simulada; multiplicación de voto; autoridad por avatar.  
**Gate:** decisión personal del representado + contrato común StateOS/Unreal + pruebas adversariales.

### PIONEER-D2-011 — Differential Digestion / herramientas de procedencia y comparación

**Estado:** `AVAILABLE_FOR_PIONEER_BUILD`  
**Base:** régimen del Palacio/Gremio de Unificación y Sistema de Pioneros.  
**Puede construirse:** registradores de procedencia, comparadores de capacidades, matrices `capacidad externa -> equivalente Rudis -> gap -> riesgo -> licencia -> beneficio`, tooling de D0/D1/D2 y paquetes de evidencia.  
**No construir:** adopción automática, autoridad externa, modificación automática del Canon o incorporación sin licencia.  
**Gate:** toda recomendación debe seguir siendo recomendación hasta disposición competente.

### PIONEER-D2-012 — Portabilidad y salida técnica D2

**Estado:** `AVAILABLE_WITH_GATES`  
**Base:** doctrina de salida/continuidad y verificabilidad externa.  
**Puede construirse:** exportadores de estado/historial simulados, formatos neutrales, migración de credenciales ordinaria, tests de read-back y reconstrucción.  
**Invariantes:** `EXPORT != MIGRATION PROVEN`; `PORTABILITY CLAIM -> PORTABILITY TEST`.  
**No construir:** prometer equivalencia jurídica externa, recovery extraordinario o migración productiva no autorizada.  
**Gate:** prueba de import/reconstruction independiente.

---

## PROYECTOS NO ABIERTOS COMO FRUTO COMPLETO

### RHEA / Mecano Hospitalaria

**Estado:** `NOT GENERALLY AVAILABLE / ASSEMBLY REVIEW`  
Puede trabajarse únicamente en herramientas neutras ya autorizadas por otros proyectos o en prototipos expresamente D2 que no inventen diagnóstico, sanción, cuarentena jurídica ni autoridad médica.

### Recovery extraordinario de identidad

**Estado:** `HOLD / REAL NORMATIVE DEPENDENCY`

### Producción, dinero real, D3/D4 y proveedores financieros reales

**Estado:** `BLOCKED`

---

## REGISTRO DE APORTACIONES — FORMATO

Cada voluntario deberá abrir o recibir una entrada:

```text
CONTRIBUTION_RECORD_ID:
PROJECT_ID:
CONTRIBUTOR:
IDENTITY_STATUS:
START_DATE:
SUBMISSION_DATE:
CONTRIBUTION_TYPE:
DESCRIPTION:
LICENSE / TERMS:
THIRD_PARTY_PROVENANCE:
ARTIFACTS:
BASELINE / TARGET STATE:
TESTS:
DECLARED_RESULTS:
KNOWN_LIMITATIONS:
CONSTRUCTION_REVIEW:
UNIFICATION_VALUATION:
COMPETITIVE_DIGESTION_DOSSIER:
ASSEMBLY_DISPOSITION:
TECHNICAL_BENEFIT_REALIZED:
RECOGNITION / BENEFIT IF ANY:
RESERVATIONS / DISPUTES:
LAST_REVIEW:
```

Estados del fruto:

`REGISTERED -> BUILDING -> SUBMITTED -> CONSTRUCTION_REVIEW -> UNIFICATION_REVIEW -> COMPETITIVE_DIGESTION -> ASSEMBLY_PENDING -> FINAL_DISPOSITION`

---

## REGLA DE ACTUALIZACIÓN

Este registro deberá actualizarse cuando:

- aparezca una nueva decisión `TECHNICAL_IMPLEMENTATION_ALLOWED`;
- una Asamblea abra/cierre un gate;
- un proyecto entre en HOLD;
- un proyecto sea superseded;
- aparezca una nueva deuda técnica construible;
- una política abierta se resuelva;
- un proyecto pase de D2 a otra fase por acto competente;
- una aportación pionera sea presentada, digerida o dispuesta.

Quien actualice deberá citar la fuente de cambio y conservar la entrada histórica si el proyecto cambia de estado.

`ACTUALIZAR != BORRAR GENEALOGÍA`

---

## CADENA SOBERANA DE ACEPTACIÓN

`VOLUNTARIO PIONERO`
`-> FRUTO`
`-> REGISTRO DE APORTACIÓN`
`-> GREMIO/PALACIO DE CONSTRUCCIÓN`
`-> PALACIO + GREMIO DE UNIFICACIÓN`
`-> DIGESTIÓN COMPETITIVA`
`-> RECOMENDACIÓN`
`-> ASAMBLEA GENERAL SOBERANA`
`-> ACCEPT / ACCEPT_PARTIAL / RETURN / REDIGEST / HOLD / REJECT`

**La lista abre trabajo. No predetermina la aceptación del resultado.**
