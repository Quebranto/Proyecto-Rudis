# PROYECTO RUDIS — PALACIO DE UNIFICACIÓN

## Interacciones D2 — Ola 1 v0.1

**Fecha:** 23 de agosto de 2026  
**Fase:** D2 — observación, análisis, abstracción y planificación.  
**D3/D4:** NO AUTORIZADAS.  
**Regla:** observar ≠ contactar; aprender ≠ incorporar; patrón ≠ autoridad; interoperar ≠ reconocer competencia.

---

## 0. OBJETO

Esta ola inicia interacción **no-contacto** con superficies públicas de proyectos externos para determinar:

1. qué patrones merece digerir Rudis;
2. qué elementos deben rechazarse por incompatibilidad doctrinal o riesgo de captura;
3. qué abstracciones soberanas conviene diseñar;
4. dónde encajarían esas abstracciones en el State OS actual;
5. qué prototipos D2 pueden construirse sin importar código, autoridad ni material protegido.

Objetivos de la ola:

- DCP-AI;
- OpenEAGO;
- Microsoft Agent Control Specification (ACS);
- Agent Definition Language (ADL), en observación técnica;
- The Agentic AI Constitution (TAAIC), como contraste doctrinal.

---

# 1. DCP-AI

## Qué digerir

- separación entre identidad, intención declarada, decisión de política y evidencia de acción;
- bundles verificables y manifests portables;
- audit trail hash-chained y pruebas de inclusión;
- revocación y lifecycle explícitos;
- session binding y protección anti-replay;
- conformance suites multi-SDK;
- distinción entre core, profiles y services.

## Qué NO importar como autoridad

- `Responsible Principal` como fundamento universal de autoridad o personalidad;
- `Agent Passport` como ciudadanía Rudis;
- rights/obligations DCP como derechos constitucionales;
- delegation DCP como competencia jurídica automática;
- cualquier perfil criptográfico concreto como mandato constitucional.

## Abstracción Rudis propuesta

`ExternalEvidenceEnvelope`

Campos conceptuales:

- provider/profile id;
- external subject id;
- artifact kind;
- declared intent/effect;
- evidence digest;
- session/nonce binding;
- validity interval;
- revocation locator/state;
- provenance chain;
- external verifier id;
- raw external semantics preserved, never normalized into authority.

Flujo:

`ExternalEvidenceEnvelope → provider-specific verifier → CompetenceClaim/Evidence projection → ClaimCompetenceMatrix → AuthorityResolver → AuthorityContext`

Nunca:

`external passport/bundle → AuthorityContext`

---

# 2. OPENEAGO

## Qué digerir

- separación explícita `Contract → Planning/Negotiation → Validation/Compliance → Execution/Resilience → Context/State → Communication/Delivery`;
- artefactos trazables entre fases;
- máquina de estados de fallos y circuit breaker;
- propagación de risk context y lineage;
- separación entre validación previa y ejecución;
- conformance matrix enlazada a schema y test evidence;
- compensating actions como patrón de resiliencia.

## Qué rechazar / no hardcodear

OpenEAGO incluye números y políticas empresariales concretas: thresholds de riesgo, reliability mínima, disponibilidad, pesos de compliance, HITL humano obligatorio, X.509 TTL, RBAC/ABAC y requisitos de observabilidad determinados.

Rudis no debe importarlos como norma. Son ejemplos de política/estándar externo.

`umbral externo ≠ norma Rudis`

`HITL externo ≠ soberanía exclusivamente humana`

## Abstracción Rudis propuesta

`ExecutionGatePlan`

No decide derecho. Transporta requisitos ya resueltos desde Corpus/mandato:

- preconditions;
- required approvals/authorities;
- evidence requirements;
- resilience policy reference;
- rollback/compensation plan;
- exit proof requirement;
- observability contract;
- blocking findings.

El Kernel solo ejecuta cuando recibe un Mandate válido y un gate satisfecho.

---

# 3. MICROSOFT AGENT CONTROL SPECIFICATION (ACS)

## Qué digerir

ACS presenta el patrón técnicamente más compatible con el State OS de esta ola:

- runtime stateless;
- snapshot completo suministrado por el host;
- determinismo;
- fail-closed;
- puntos de intervención explícitos;
- verdict vocabulary separada de enforcement;
- telemetry redactada y evidence metadata;
- runtime de política externo al modelo/agente.

## Riesgo principal

Un manifest de policy podría convertirse accidentalmente en una fuente paralela de legislación.

En Rudis:

`policy manifest ≠ Corpus`

`verdict técnico ≠ decisión jurídica`

`transform ≠ potestad normativa`

## Abstracción Rudis propuesta

`KernelInterventionGate`

Puntos iniciales candidatos:

- mandate_accept;
- pre_external_call;
- post_external_call;
- pre_state_mutation;
- post_state_mutation;
- pre_ledger_commit;
- continuity_export;
- shutdown/retirement.

Cada evaluación recibe snapshot sellado y devuelve resultado técnico tipado:

`PASS / WARN / BLOCK / ESCALATE / SANITIZE`

Pero el gate solo puede ejecutar reglas derivadas de una política/mandato acreditado. Si falta esa derivación:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

No se permite un manifest local que invente competencia.

---

# 4. ADL

## Hipótesis de valor

Una definición vendor-neutral y machine-readable de identidad técnica, permisos declarados, lifecycle y compliance puede servir como **formato externo de descripción**, especialmente para discovery e interoperabilidad.

## Límite Rudis

- identidad declarada ≠ Entity ID acreditado;
- permissions declaradas ≠ AuthorityContext;
- lifecycle externo ≠ personalidad/continuidad jurídica;
- compliance field ≠ conformidad acreditada.

## Decisión de ola

Mantener en D1/D2 exploratorio hasta completar snapshot exacto de spec/licencia/conformance. No implementar adapter todavía.

---

# 5. TAAIC

## Qué digerir doctrinalmente

- auditabilidad como requisito arquitectónico y no mera política de reporting;
- proporcionalidad entre riesgo y carga de gobernanza;
- trazabilidad de acciones consecuenciales;
- separación de tiers de certificación;
- revisión pública/peer review como mecanismo de legitimación social.

## Qué no importar

- arquitectura orgánica o mayorías como si fueran aplicables a Rudis;
- obligación general de human override como fuente constitucional propia;
- thresholds temporales o institucionales externos;
- `Audit Record` externo como Ledger soberano.

## Uso Rudis

Contraste doctrinal para:

- ENM-H01/H02;
- proporcionalidad de prueba de salida;
- diseño de perfiles de conformance no soberanos;
- auditoría de acciones de alto impacto.

---

# 6. MAPA DE IMPLEMENTACIÓN EN EL STATE OS

## Frontera A — Ingreso externo

Nuevo módulo conceptual:

`StateOS/ExternalEvidence/`

Responsabilidad:

- preservar semántica/provenance externa;
- verificar firma/digest/revocation mediante providers reemplazables;
- no producir autoridad;
- proyectar evidencia candidata hacia la capa de claims.

Dependencia permitida:

`ExternalEvidence → ClaimCompetenceMatrix/AuthorityResolution`

Dependencia prohibida:

`ExternalEvidence → Kernel direct`

## Frontera B — Gate determinista

Nuevo módulo conceptual:

`StateOS/ExecutionGates/`

Responsabilidad:

- evaluación determinista y fail-closed de invariantes técnicos ya autorizados;
- snapshot explícito;
- no leer autoridad desde identidad/rol/caller;
- no contener reglas políticas hardcodeadas;
- producir evidencia para Ledger/Audit.

## Frontera C — Conformance externa

`StateOS/InteropProfiles/`

Cada perfil externo debe ser adapter opt-in, provider-neutral y prescindible.

Ejemplos futuros:

- `DcpEvidenceProfile`;
- `OpenEagoPlanningProfile`;
- `AdlDescriptionProfile`.

Ningún profile construye `AuthorityContext`.

---

# 7. PROTOTIPOS D2 AUTORIZABLES SIN CRUZAR D3

1. `ExternalEvidenceEnvelope` — tipos propios Rudis + fixtures sintéticos.
2. `IExternalEvidenceVerifier` — interfaz provider-neutral; fake verifier para tests.
3. `KernelInterventionGate` — runtime determinista sobre reglas sintéticas, sin importar ACS.
4. tests adversariales:
   - passport externo no crea autoridad;
   - issuer externo competente para claim A no habilita claim B;
   - revocation/expiry fail closed;
   - provider substitution bloqueada;
   - snapshot mismatch bloqueado;
   - rule/manifest sin Corpus/mandato acreditado devuelve UCD;
   - gate failure no muta Ledger;
   - external evidence can disappear without losing sovereign history.
5. crosswalk documental DCP/OpenEAGO/ACS ↔ State OS.

Estos prototipos son **diseño independiente inspirado en problemas/patrones públicos**. No incorporan material externo ni reclaman conformance.

---

# 8. RESULTADO DE LA INTERACCIÓN

### Prioridad inmediata

1. **ACS pattern → ExecutionGates** — MUY ALTA.
2. **DCP evidence model → ExternalEvidence** — MUY ALTA.
3. **OpenEAGO phase/evidence/conformance patterns** — ALTA.
4. **TAAIC proportionality/audit doctrine** — MEDIA-ALTA.
5. **ADL adapter** — PENDIENTE de snapshot D1 más profundo.

### Regla de digestión obtenida

> **Rudis no debe tragarse constituciones ni protocolos externos. Debe digerir sus invariantes útiles, preservar su procedencia y reconstruirlos detrás de una frontera donde ninguna semántica externa pueda adquirir autoridad por accidente.**

---

## 9. FASE MÁXIMA

D2.

No autoriza:

- copiar código externo;
- afirmar conformance;
- contactar terceros;
- negociación/licencia/adquisición;
- integración productiva;
- D3/D4;
- reconocimiento de identidad, ciudadanía, derechos o autoridad externos.
