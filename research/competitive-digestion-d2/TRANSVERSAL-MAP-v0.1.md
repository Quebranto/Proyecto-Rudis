# Mapa competitivo transversal v0.1

Este mapa compara propiedades; no homologa vocabularios ni importa autoridad.

## Lectura transversal

| Superficie | OAGS | OpenEAGO | ACP | OpenAGP | Anumati/ACAP | Postura Rudis |
|---|---|---|---|---|---|---|
| Identidad | Fingerprint de modelo/prompt/tools | X.509, OIDC, mTLS, registry | UID/proceso Linux | Actor/vendor/plane + claves | Identidad A2A/DID asumida | Puede entrar como `ExternalEvidence`; nunca como competencia |
| Política | Declarativa y local | Control plane regulado y risk profiles | YAML allow/ask/deny | Policy cross-vendor | PolicyDocument/ODRL del callee | Política externa describe una regla externa; no legisla Rudis |
| Enforcement | SDK/runtime local | Validación + HITL + orquestación | nftables + proxy | Vendor receiver / decision callback | Middleware caller/callee | Sólo `ExecutionGates` acreditados pueden afectar ejecución Rudis |
| Evidencia | Eventos firmados/conformance | Artefactos por fase y KPI | JSONL sin integridad criptográfica | Eventos firmados/canónicos | Consent chain + AdherenceEvent | Ingreso por `ExternalEvidence`; Ledger auxiliar != Ledger soberano |
| Revocación/versionado | Identidad cambia con configuración | Certificados/perfiles/contratos | TTL corto de aprobación host | Política y actores versionados | Version bump exige reaceptación | Snapshot exacto, no fallback ni downgrade |
| Autoridad implícita peligrosa | Registry/verifier/policy verdict | board/legal refs, risk score, roles empresariales | humano/canal aprueba red | customer plane decide | agent/principal acepta términos | Ninguna se convierte en `AuthorityContext` o `VerifiedLawDecision` |

## Qué hace cada proyecto mejor que Rudis hoy

### OAGS

- Define un fingerprint reproducible de configuración de agente.
- Publica formatos y vectores de conformance sobre identidad, firma y política.
- Diseña enforcement local/offline como requisito de base.

Brecha propia: su supuesto de canonicalización JSON por orden de parseo no es una canonicalización interlenguaje suficiente, y el harness público no es autocontenido.

### OpenEAGO

- Tiene la arquitectura documental más amplia: contrato, negociación, validación, ejecución, contexto y entrega.
- Propaga riesgo, SLA/SLO y evidencia entre fases.
- Mantiene schemas versionados, ejemplos, proceso FINOS, Security y gobierno técnico explícitos.

Brecha propia: mezcla arquitectura de control con política empresarial concreta. Umbrales, `board_approval_ref`, `legal_review_ref`, reputación y perfiles no son transportables como autoridad.

### ACP

- Demuestra una barrera real de kernel para egress, no sólo una declaración de consentimiento.
- Su threat model reconoce con precisión qué no puede observar.
- Falla cerrado si el proxy no está disponible.

Brecha propia: herramientas server-side eluden la mediación; el agente puede modificar policy/audit en la configuración por defecto; HTTPS se decide a nivel host; no hay firma ni hash-chain en v0.3.0.

### OpenAGP

- Separa tres flujos: evento, distribución de política y decisión síncrona.
- Diseña schemas y test vectors cross-language.
- Distingue niveles de conformance y licencias por tipo de activo.

Brecha propia: un registry y un control plane del cliente pueden convertirse en raíz de confianza central; Flow C puede crear una segunda ruta de decisión si se conecta directamente al Kernel.

### Anumati / ACAP

- Separa capability/auth de usage policy.
- Vincula policy version, consentimiento y evidencia por acción.
- Aporta modelo TLA+ acotado y validadores pequeños.
- Su callee valida en frontera, en lugar de confiar únicamente en self-policing del caller.

Brecha propia: JWS está fuera de v0.1; append-only es por convención; el reasoning es inicialmente autoatestado; sus conclusiones legales no quedan probadas por la estructura técnica.

## Patrones absorbibles sin importar semántica política

1. **Fingerprint de artefacto compuesto**, con canonicalización normativa segura y perfil criptográfico externo.
2. **Policy snapshot versionado** y rechazo explícito de downgrade/staleness.
3. **Evidence-by-phase** para reconstruir por qué una operación avanzó o se detuvo.
4. **Per-action evidence** ligada al payload y a la regla exacta evaluada.
5. **Fail-closed mediation** fuera del proceso que puede mentir.
6. **Conformance vectors** autocontenidos y cross-language.
7. **Threat models que enumeren bypasses conocidos**, no sólo garantías deseadas.
8. **Separación entre passive events, policy transport y synchronous decision**, manteniendo los dos últimos fuera de la fuente jurídica Rudis.

## Patrones que deben quedar aislados

- identidad basada únicamente en prompt/model/tools;
- trust score, reliability score o registry membership como competencia;
- aprobación humana de una petición técnica como mandato jurídico;
- policy/control plane externo conectado directamente al Kernel;
- self-attestation de adherencia tomada como prueba suficiente;
- `board`, `legal reviewer`, vendor, customer o principal externo como rol constitucional Rudis;
- audit log externo como historia soberana;
- conformance level como acreditación productiva;
- semántica legal declarada por una especificación técnica como Canon.

## Rutas Rudis permitidas

```text
external identity/config fingerprint
        -> ExternalEvidenceEnvelope
        -> exact provider/verifier + snapshot
        -> VerifiedExternalEvidence
        -> candidate projection
        -> ClaimCompetenceMatrix route
        -> AuthorityResolver
```

No existe ruta permitida:

```text
external registry/policy/consent/verdict -> AuthorityContext
external decision callback -> SovereignKernel
external audit chain -> ContinuityLedger head
```

## Conclusión transversal

Los cinco proyectos convergen en el seam correcto — identidad, policy, enforcement y evidencia — pero ninguno responde por Rudis a la pregunta constitucional de quién tiene competencia. Su mejor aportación conjunta es técnica: hacer más verificable la evidencia que llega a una ruta de autoridad ya acreditada.

`mejor evidencia externa != nueva fuente de autoridad`


