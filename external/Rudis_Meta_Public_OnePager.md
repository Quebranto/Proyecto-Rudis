# Rudis Ecosystem — Public One-Pager

## What Rudis is

Rudis is an experimental constitutional and systems-architecture project exploring how software, agents, institutions and interactive environments can share one governed state without allowing interfaces, runtime control, identity assertions or technical capability to silently become authority.

Its central engineering problem is simple to state:

> A representation of state does not acquire authority over reality merely by claiming to represent it.

Rudis therefore separates identity, evidence, competence, authority, legal/rule evaluation, mandate, execution, continuity and audit as distinct concerns.

## Core architecture

At a public high level, the execution path is:

```text
ACTOR / CLIENT
    -> INTENT
    -> IDENTITY / CLAIM
    -> COMPETENCE / AUTHORITY RESOLUTION
    -> LAW / RULE EVALUATION
    -> MANDATE
    -> SOVEREIGN EXECUTION
    -> RECEIPT / EFFECT
    -> CONTINUITY
    -> AUDIT / OBSERVABILITY
```

Key invariants:

- `IDENTITY != COMPETENCE`
- `EVIDENCE != AUTHORIZATION`
- `REPRESENTATION != AUTHORITY`
- `CLIENT INTENT != SOVEREIGN DECISION`
- `CI GREEN != ACCREDITATION`
- `MERGE != PRODUCTION`

## Why this matters

Many modern agentic or distributed systems collapse several of these layers into one trusted runtime, SDK, account, token, UI or policy engine. Rudis investigates a stricter model in which technical capability never becomes political or institutional authority by accident.

This makes Rudis relevant to questions such as:

- governed multi-agent systems;
- durable identity and authority separation;
- replay, revocation and stale-state handling;
- auditable causal execution;
- safe representation of sovereign state in clients and virtual worlds;
- recovery without fabricating authority;
- provider and engine neutrality;
- independent falsification of security and governance claims.

## Current maturity

Rudis has:

- a public constitutional / architectural Corpus;
- a private implementation under active development;
- a PRE-D3 campaign focused on integration, reproducibility, recovery, security and independent falsification.

Current public maturity statement:

```text
PRE-D3 = ACTIVE
D3 OPEN = NO
PRODUCTION = NO
REAL CUSTOMERS = NO
REAL MONEY = NO
```

Component-level technical progress must not be confused with global accreditation or production readiness.

## Security and disclosure posture

Rudis is designed to be auditable without making its public repository an attack inventory.

Public material may include architecture, contracts, invariants, decisions, sanitized audit outcomes, known limitations and HOLD states.

Private operational details such as credentials, private repository locators, branches, hashes, CI identifiers, sensitive internal paths, exploit recipes and unnecessary personal data are not published by default.

`TRANSPARENCY != UNRESTRICTED OPERATIONAL DISCLOSURE`

## Evaluation

External technical evaluation is welcome when it preserves:

- factual maturity;
- provenance;
- minimum necessary disclosure;
- separation between private evidence and public claims;
- explicit treatment of failures, reservations and residual risk.

Rudis does not treat external interest, an NDA, a successful build, a merge or a security review as automatic authority to open D3 or production.

## Public starting points

Use the public repository as the canonical external entry point for:

- Corpus and architecture;
- current public decisions;
- PRE-D3 gate definitions;
- public security/disclosure policy;
- sanitized audit history.

For deeper technical review, access should be purpose-bound and progressively disclosed rather than granted as unrestricted repository access.
