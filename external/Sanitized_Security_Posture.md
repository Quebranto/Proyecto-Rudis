# Rudis — Sanitized Security Posture

## Purpose

This document summarizes the public security posture of Rudis for external technical evaluation without exposing private operational details.

It is not a penetration-test report and does not assert that Rudis is fully secure.

## Public security principles

Rudis distinguishes constitutional transparency from unrestricted operational transparency.

```text
TRANSPARENCY != UNRESTRICTED OPERATIONAL DISCLOSURE
ACCESS AUTHORIZED != PUBLICATION AUTHORIZED
PRIVATE TRACEABILITY != PUBLIC DISCLOSURE
SANITIZE EVIDENCE != ALTER FINDING
```

Public reporting must preserve adverse findings, HOLD states, reservations and residual risk while removing unnecessary operational metadata.

## Security themes under active evaluation

The PRE-D3 campaign includes work on:

- identity / competence separation;
- authority freshness and revocation;
- replay, duplicate delivery and stale-state rejection;
- mandate and authority-context fabrication resistance;
- causal traceability from decision to effect;
- continuity, restart and recovery without invented authority;
- client / world boundaries that cannot become sovereign paths;
- test/simulation contamination boundaries;
- multi-client consistency;
- secret scanning and CI privilege minimization;
- dependency/provenance review;
- process, filesystem and IPC boundaries;
- logging/crash-dump review;
- reproducible builds and artifact provenance.

## Public disclosure form for findings

A finding may be reported publicly as:

```text
PROPERTY
RISK
STATUS
SEVERITY
EXIT CONDITION
D3 IMPACT
```

Private by default:

- exact private repository locations;
- private branch names;
- private hashes or heads;
- private CI identifiers or URLs;
- sensitive internal paths;
- private diffs and code;
- detailed exploit recipes while a vulnerability is open;
- credentials, tokens, keys or secrets;
- unnecessary infrastructure/account identifiers;
- unnecessary personal data.

## Evidence discipline

Rudis does not treat the following as equivalent:

```text
BUILD GREEN != SECURITY ACCREDITATION
SELF-REPORT != INDEPENDENT EVIDENCE
FIX IMPLEMENTED != FIX REATTACKED
COMPONENT PASS != SYSTEM PASS
```

Security-relevant properties are expected to move through build/test, adversarial review, repair where needed, independent verification and explicit disposition.

## Known posture limitations

The public repository does not expose the complete private implementation or complete private security evidence. Therefore, public observers can assess architecture, invariants, process discipline, sanitized findings and public evidence, but not independently reconstruct every private technical claim from public material alone.

This is intentional and should not be interpreted as proof of either correctness or absence of implementation.

## Current operational claim

The safe external statement is:

> Rudis is actively hardening and falsifying its PRE-D3 candidate. It preserves public evidence of findings and limits while keeping sensitive implementation and exploit details purpose-bound. Whole-system security accreditation and D3 opening have not been declared.

```text
PRE-D3 = ACTIVE
D3 OPEN = NO
PRODUCTION = NO
```
