# Threat model transversal v0.1

## Activos protegidos

1. unicidad de la ruta `AuthorityResolver -> LawEngine -> Mandate -> Kernel -> Continuity`;
2. separación entre evidencia externa y autoridad;
3. exactitud de snapshot, versión, sujeto, acción, payload, regla y contexto;
4. historia soberana append-only;
5. separación Simulation/Production;
6. procedencia y obligaciones de licencia.

## Adversarios y fallos

- proveedor externo malicioso;
- registry comprometido;
- verifier técnicamente compatible pero no acreditado;
- policy publisher que hace downgrade o equivocation;
- agente que autoatesta adherencia falsa;
- control plane que devuelve `allow` para semántica no autorizada;
- humano/canal comprometido que aprueba una petición distinta;
- adapter honesto pero desactualizado;
- canonicalización divergente entre lenguajes;
- build que enlaza un fake o bypass experimental;
- componente que presenta conformance como autoridad.

## Ataques comunes y respuesta requerida

| Ataque | Ejemplo competitivo | Respuesta Rudis |
|---|---|---|
| Identity substitution | SekuireID o actor AGP sustituido | Bind exact provider, verifier, digest, subject y snapshot; no crear competencia |
| Canonical ambiguity | JSON por orden de parseo | Canonicalización normativa única; bytes de test cross-language |
| Policy downgrade | policy/version antigua | Exact version range + active Corpus/context; fail closed |
| Registry capture | registry de agentes/keys | Registry sólo produce evidencia; autoridad acreditadora separada |
| Verifier capture | vendor/plane valida su propio resultado | Vincular verifier exacto al requisito; éxito no concede competencia |
| Decision-path injection | OpenAGP Flow C o OpenEAGO control plane | Adapter termina en evidence/gate; nunca llama directamente a Kernel |
| Consent inflation | ACP approval o ACAP ConsentRecord | Tipar como `ProtocolConsentEvidence`; nunca `AuthorizationMandate` |
| Self-attestation | AdherenceEvent del caller | Corroboración del callee/telemetría; indeterminado falla cerrado |
| Replay/cross-context | aprobación host cacheada o consent chain reutilizada | Bind nonce/context/action/payload/snapshot; TTL no sustituye binding |
| Audit sovereignty confusion | JSONL/hash chain externo | Auxiliary evidence store; no modifica sovereign head |
| Simulation leakage | harness/SDK fake enlazado | Build graph y packaging separados; negative CI gate |
| Legal-semantic import | UETA/GDPR/board role declarado | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` cuando se requiera decisión política |

## Challenge suite D2 propuesta

Los prototipos futuros deberán probar al menos:

1. dos serializadores producen bytes distintos para el mismo objeto: rechazo;
2. key/actor correcto con policy equivocada: rechazo;
3. policy correcta, versión obsoleta: rechazo;
4. evento válido reutilizado con otro payload/sujeto/contexto: rechazo;
5. verifier alternativo con la misma interfaz: rechazo;
6. registry comprometido anuncia actor técnicamente válido: no crea competencia;
7. control plane externo devuelve `allow`: no produce Mandate;
8. ConsentRecord/AdherenceEvent válido: permanece `ExternalEvidence`;
9. audit chain válida pero separada del Ledger: no reconstruye historia soberana;
10. provider unavailable/indeterminate: fail closed;
11. fake de conformance en artefacto productivo: fallo de build/package;
12. fuente externa cambia durante una resolución: se conserva un único snapshot.

## Capture audit inicial de OpenEAGO

Promoción futura queda bloqueada si no se demuestra:

- sustitución del proveedor/control plane sin tocar lógica soberana;
- exportación auditable de contratos, decisiones y evidencia;
- degradación fail-closed si registry, HITL, telemetry o policy engine fallan;
- eliminación de roles/umbrales empresariales del núcleo Rudis;
- imposibilidad de que `board_approval_ref`, `legal_review_ref`, risk score o reputation creen competencia;
- separación verificable entre fallback técnico y nueva autorización;
- ausencia de un segundo commit path desde el orquestador.

## Riesgos residuales

Este artefacto no reproduce todavía las suites upstream ni verifica todas sus afirmaciones de rendimiento, model checking o cross-language parity. Esas tareas son dependencias de investigación, no UCD. Las consecuencias jurídicas positivas de consentimiento, adherencia, contrato o representación siguen siendo UCD donde el Corpus no las determine.


