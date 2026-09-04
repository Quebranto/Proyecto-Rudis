# External Disclosure Classification Matrix

## Purpose

This matrix defines the default disclosure level for material considered for external review, including conversations with Meta or other technical/commercial evaluators.

It is a publication-control aid, not a grant of access.

`CLASSIFICATION != AUTHORIZATION`

`NDA != UNLIMITED ACCESS`

## Levels

| Level | Meaning | Default audience |
|---|---|---|
| `PUBLIC` | Safe to publish without additional operational disclosure | General public |
| `PUBLIC_AFTER_SANITIZATION` | May be published after removing unnecessary sensitive metadata/details | General public |
| `NDA_ONLY` | May be shared only under an appropriate NDA and purpose-bound review | Approved external reviewers |
| `RESTRICTED_REVIEW` | Requires explicit need-to-know, minimal access and controlled handling | Named technical reviewers |
| `DO_NOT_SHARE` | Not suitable for external disclosure absent a new explicit decision | Internal only |

## Default matrix

| Information class | Default level | Public representation |
|---|---|---|
| Canon / constitutional texts | `PUBLIC` | Full public text when already public |
| Public architecture principles | `PUBLIC` | Full high-level architecture |
| Public invariants | `PUBLIC` | Full invariant statements |
| PRE-D3 gates and public status | `PUBLIC` | Current factual status |
| Public issue decisions | `PUBLIC` | Full public record, subject to historical sanitization |
| Known HOLD / FAIL / limitations | `PUBLIC` | Preserve substance and impact |
| Sanitized audit conclusions | `PUBLIC` | Property, result, severity, exit condition, impact |
| Threat model themes | `PUBLIC_AFTER_SANITIZATION` | Attack class without operational recipe |
| Detailed technical diagrams | `NDA_ONLY` by default | High-level version public |
| Exact candidate identity | `RESTRICTED_REVIEW` | “controlled candidate” publicly |
| Reproducibility evidence | `NDA_ONLY` / `RESTRICTED_REVIEW` depending on detail | Sanitized summary publicly |
| Private source code | `RESTRICTED_REVIEW` | Architecture/contract only publicly |
| Private repository locator | `DO_NOT_SHARE` by default | “private Forge” |
| Private branch names | `DO_NOT_SHARE` by default | Omit |
| Private commit hashes / heads | `DO_NOT_SHARE` by default | Omit |
| Private CI IDs / URLs | `DO_NOT_SHARE` by default | Result summary only |
| Sensitive internal paths | `DO_NOT_SHARE` by default | Component/property only |
| Internal diffs | `RESTRICTED_REVIEW` | Finding/fix summary publicly |
| Open vulnerability exploit recipe | `DO_NOT_SHARE` / controlled responsible disclosure | Risk + status + exit condition |
| Closed vulnerability technical history | `NDA_ONLY` or sanitized public summary | Preserve existence and outcome |
| Credentials / tokens / private keys | `DO_NOT_SHARE` | Never publish |
| Production secrets | `DO_NOT_SHARE` | Never publish |
| Crash dumps containing sensitive data | `DO_NOT_SHARE` | Sanitized diagnostic summary |
| Internal hosts / endpoints / account identifiers | `DO_NOT_SHARE` unless strictly required | Functional description |
| PII unnecessary to evaluation | `DO_NOT_SHARE` | Remove |
| Public author attribution already intentionally published | `PUBLIC` | Preserve provenance |
| IP / license inventory | `PUBLIC_AFTER_SANITIZATION` or `NDA_ONLY` depending on contract detail | Category + license/provenance status |
| Third-party confidential terms | `DO_NOT_SHARE` unless agreement permits | Existence/status only |
| Demo screenshots / video | `PUBLIC_AFTER_SANITIZATION` | Only real state/capabilities, no internals |
| Mock / fixture / simulation | `PUBLIC_AFTER_SANITIZATION` | Must be explicitly labelled |

## Finding disclosure template

For unresolved or recently repaired security findings, the default public form is:

```text
PROPERTY
RISK
STATUS
SEVERITY
EXIT CONDITION
D3 IMPACT
```

The following remain private by default:

```text
EXACT PRIVATE LOCATION
PRIVATE CODE
EXPLOIT SEQUENCE
BOUNDARY VALUES THAT MATERIALIZE THE EXPLOIT
INTERNAL HOST / CI TOPOLOGY
CREDENTIAL MATERIAL
```

## Meta-specific progressive disclosure

### Stage 1 — Initial discussion

Permitted:

- public repository;
- public one-pager;
- RAL Public Architecture Brief;
- current maturity/limits;
- public security posture;
- sanitized demo material;
- public provenance/IP inventory.

### Stage 2 — NDA technical diligence

May add, after review:

- detailed architecture diagrams;
- sanitized threat model;
- selected audit evidence;
- reproducibility summary;
- license/IP matrix with non-public detail where disclosure is permitted;
- residual-risk register;
- selected technical contracts.

### Stage 3 — Restricted technical review

May add only with explicit scope and named reviewers:

- exact candidate;
- selected private implementation;
- reproducibility artifacts;
- detailed vulnerability evidence under responsible disclosure;
- controlled logs and test artifacts.

No stage grants unrestricted access automatically.

## Pre-flight rule

Before releasing any external artifact, verify:

```text
FACTUALLY CURRENT
+ CORRECT CLASSIFICATION
+ SANITIZED WHERE REQUIRED
+ NO UNNECESSARY PII
+ NO SECRET MATERIAL
+ NO EXCESS OPERATIONAL METADATA
+ MATURITY NOT OVERSTATED
+ FAIL/HOLD PRESERVED
+ PROVENANCE / LICENSE CHECKED
+ PURPOSE-BOUND DISCLOSURE
= RELEASE CANDIDATE
```

Any unresolved material question results in:

`HOLD DISCLOSURE`

until reviewed.
