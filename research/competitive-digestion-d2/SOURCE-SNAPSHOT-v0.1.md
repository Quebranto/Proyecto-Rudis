# Campaña D2 de digestión competitiva — Snapshot de fuentes v0.1

Fecha de corte: 24 de agosto de 2026  
Autor técnico: Hephaestus / Codex  
Autoridad: Issue #32; D2 documental y experimental únicamente.

Este registro fija identidades y commits para que una sigla no sustituya a la procedencia. No acredita, adopta ni reconoce autoridad externa.

`nombre informal != identidad del expediente`

`snapshot estudiado != versión acreditada por Rudis`

## Fuentes primarias fijadas

| Expediente | Identidad técnica estudiada | Snapshot | Versión declarada | Licencia observada | Estado de fuente |
|---|---|---|---|---|---|
| OAGS | [sekuire/oags](https://github.com/sekuire/oags) | [`e00031d39d51e010d77d0fb7ccccd9b81d79aece`](https://github.com/sekuire/oags/tree/e00031d39d51e010d77d0fb7ccccd9b81d79aece) | OAGS 0.1.1, Draft | Apache-2.0 | Identidad resuelta |
| OpenEAGO | [finos-labs/open-eago](https://github.com/finos-labs/open-eago) | [`f03627fce810a8e0ba423147fe29a854b5fcd3b2`](https://github.com/finos-labs/open-eago/tree/f03627fce810a8e0ba423147fe29a854b5fcd3b2) | 0.1 / schemas v0.1.0 | Apache-2.0 | Identidad resuelta |
| ACP | [o1100/Agent-Consent-Protocol](https://github.com/o1100/Agent-Consent-Protocol) | [`06c563237c9e0803afc0730cef5935ed49db2fb8`](https://github.com/o1100/Agent-Consent-Protocol/tree/06c563237c9e0803afc0730cef5935ed49db2fb8) | 0.3.0, working prototype | Apache-2.0 | Candidato resuelto por contexto; sigla ambigua |
| OpenAGP | [openagp/spec](https://github.com/openagp/spec) | [`c8fb613f13d46673cdaeb6ae109177ca74547222`](https://github.com/openagp/spec/tree/c8fb613f13d46673cdaeb6ae109177ca74547222) | 0.1, working draft | CC-BY-4.0 para spec; SDK/CTS declaran Apache-2.0 | Identidad resuelta; ecosistema multirrepo |
| Anumati / ACAP | [ravikiran438/agent-consent-protocol](https://github.com/ravikiran438/agent-consent-protocol) | [`fafc24a1872596e8b8438125b9d0618d1dfb7a3f`](https://github.com/ravikiran438/agent-consent-protocol/tree/fafc24a1872596e8b8438125b9d0618d1dfb7a3f) | 0.1.0-draft | Apache-2.0 | `IDENTITY_CANDIDATE` |

## Resolución de colisiones nominales

### ACP

Existen múltiples proyectos públicos llamados ACP, incluyendo Agent Communication Protocol, Agent Client Protocol y Agent Control Protocol. En esta campaña `ACP` significa exclusivamente `o1100/Agent-Consent-Protocol@06c5632`, porque el contexto de #30–#32 es consentimiento y autorización humana. Toda referencia futura deberá usar el nombre completo y el commit.

### Anumati

Existen al menos dos superficies distintas:

1. Anumati/ACAP, extensión de consentimiento y adherencia para A2A, repositorio de `ravikiran438`;
2. Anumati de IIIT-B, sistema de consentimiento y flujo de datos para DPI.

El primer candidato coincide con el vocabulario `consent/adherence` de la Asamblea y es el estudiado aquí. La identidad permanece `IDENTITY_CANDIDATE` hasta confirmación registral competente. El proyecto IIIT-B no se mezcla ni se descarta: queda como homónimo fuera del alcance de este snapshot.

## Evidencia primaria mínima

### OAGS

- [Especificación 0.1.1](https://github.com/sekuire/oags/blob/e00031d39d51e010d77d0fb7ccccd9b81d79aece/specs/oags-v0.1.md)
- [Harness de conformance](https://github.com/sekuire/oags/blob/e00031d39d51e010d77d0fb7ccccd9b81d79aece/specs/conformance-harness.md)
- [Licencia](https://github.com/sekuire/oags/blob/e00031d39d51e010d77d0fb7ccccd9b81d79aece/LICENSE)

### OpenEAGO

- [Especificación](https://github.com/finos-labs/open-eago/blob/f03627fce810a8e0ba423147fe29a854b5fcd3b2/SPECIFICATION.md)
- [Modelo machine-readable](https://github.com/finos-labs/open-eago/blob/f03627fce810a8e0ba423147fe29a854b5fcd3b2/spec/v0.1.0/spec.json)
- [Security](https://github.com/finos-labs/open-eago/blob/f03627fce810a8e0ba423147fe29a854b5fcd3b2/SECURITY.md)
- [Governance](https://github.com/finos-labs/open-eago/blob/f03627fce810a8e0ba423147fe29a854b5fcd3b2/GOVERNANCE.md)

### ACP

- [Especificación 0.3.0](https://github.com/o1100/Agent-Consent-Protocol/blob/06c563237c9e0803afc0730cef5935ed49db2fb8/SPEC.md)
- [Threat model](https://github.com/o1100/Agent-Consent-Protocol/blob/06c563237c9e0803afc0730cef5935ed49db2fb8/THREAT-MODEL.md)
- [Security](https://github.com/o1100/Agent-Consent-Protocol/blob/06c563237c9e0803afc0730cef5935ed49db2fb8/SECURITY.md)

### OpenAGP

- [Concepto y especificación](https://github.com/openagp/spec/blob/c8fb613f13d46673cdaeb6ae109177ca74547222/concept-and-spec.md)
- [Schemas](https://github.com/openagp/spec/tree/c8fb613f13d46673cdaeb6ae109177ca74547222/schemas)
- [Test vectors](https://github.com/openagp/spec/tree/c8fb613f13d46673cdaeb6ae109177ca74547222/test-vectors)

### Anumati / ACAP

- [Especificación narrativa](https://github.com/ravikiran438/agent-consent-protocol/blob/fafc24a1872596e8b8438125b9d0618d1dfb7a3f/docs/specification.md)
- [Definición normativa proto](https://github.com/ravikiran438/agent-consent-protocol/blob/fafc24a1872596e8b8438125b9d0618d1dfb7a3f/specification/consent.proto)
- [Modelo TLA+](https://github.com/ravikiran438/agent-consent-protocol/blob/fafc24a1872596e8b8438125b9d0618d1dfb7a3f/specification/ConsentLifecycle.tla)
- [Estado declarado](https://github.com/ravikiran438/agent-consent-protocol/blob/fafc24a1872596e8b8438125b9d0618d1dfb7a3f/STATUS.md)

## Incertidumbres que impiden una acreditación superior

1. OAGS referencia su runner canónico mediante una ruta local absoluta y un workspace hermano no incluido en el snapshot público. Sus vectores están publicados, pero la afirmación de conformance no es todavía reproducible desde el repositorio aislado.
2. OpenEAGO tiene artefactos y gobernanza más maduros, pero sus perfiles empresariales incorporan umbrales y roles que no pueden convertirse en autoridad Rudis.
3. ACP es un prototipo específico de Linux/OpenClaw y reconoce bypasses estructurales.
4. OpenAGP distribuye la evidencia entre varios repositorios con licencias diferentes; este snapshot sólo fija la especificación.
5. `STATUS.md` de ACAP conserva texto temporal desactualizado (afirma que el repo aún no se ha publicado aunque el snapshot existe). Sus afirmaciones de tests/model checking deben reproducirse independientemente antes de promoción.

## Estado Radar recomendado tras identificación

- OAGS: mantener `D2 documental condicionado`.
- OpenEAGO: mantener `(D2-candidate estudio, D1 acreditación Rudis, sin efectos materiales)`.
- ACP: promover de D0 a `D1 expediente`, no D2.
- OpenAGP: `D1-pending`; promoción condicionada a reproducción CTS, threat model y snapshot multirrepo.
- Anumati/ACAP: `D1-pending`; no promover hasta resolver identidad, reproducir pruebas y separar efectos jurídicos reclamados de garantías técnicas.


