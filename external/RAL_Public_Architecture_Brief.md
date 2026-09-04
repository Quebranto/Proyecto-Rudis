# RAL — Public Architecture Brief

## Purpose

This document is the public, non-sensitive architecture brief for RAL within the Rudis Ecosystem. It describes the trust and authority boundaries that may be discussed externally without exposing private implementation details.

It is not a production-readiness claim, a complete implementation specification or a substitute for private technical evidence.

## Architectural thesis

RAL separates representation from authority and requires causal traceability from an actor's intent to any state-changing effect.

Public reference path:

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

The important property is not the exact naming of modules. The property is that no upstream convenience layer can silently collapse into sovereign execution.

## Public invariants

### Identity boundary

```text
IDENTITY != COMPETENCE
AUTHENTICATION != AUTHORITY
KEY != ENTITY
```

Possessing an identity, credential, session, device or representation does not itself establish permission to cause a sovereign effect.

### Evidence boundary

```text
EVIDENCE != AUTHORIZATION
VERIFICATION != LEGISLATION
SIGNED DATA != TRUE DATA
```

Evidence may support a decision, but it does not become a decision merely because it is validly formatted, signed or externally verified.

### Representation boundary

```text
REPRESENTATION != AUTHORITY
UI STATE != SOVEREIGN STATE
CLIENT INTENT != SOVEREIGN DECISION
```

Clients, UI layers, virtual worlds and protocol adapters may request, observe and represent. They do not gain sovereign power by existing.

### Decision and execution boundary

```text
RULE EVALUATION -> MANDATE -> EXECUTION
```

A state-changing effect must be attributable to a valid decision path and a mandate that the execution boundary can verify. Alternate paths that fabricate or bypass this relationship are defects, not tolerated shortcuts.

### Continuity boundary

```text
RECOVERY != NEW AUTHORITY
RESTART != REAUTHORIZATION
STALE STATE != CURRENT STATE
```

Persistence and recovery mechanisms must preserve known state without silently creating competence or authority that did not exist before failure.

### Accreditation boundary

```text
IMPLEMENTED != ACCREDITED
CI GREEN != ACCREDITATION
MERGE != PRODUCTION
D3 READY != D3 OPEN
```

Technical evidence is necessary but not sufficient for political or operational authorization.

## Public threat model themes

RAL is designed to be falsified against classes of failure including:

- stale authority;
- replay and duplicate delivery;
- cross-session reuse;
- identity / competence conflation;
- authority-context fabrication;
- mandate fabrication;
- alternate sovereign execution paths;
- state recovery that invents authority;
- representation layers mutating authoritative state;
- test or simulation behavior contaminating production-oriented composition;
- evidence that is internally coherent but not authentic to the authoritative state.

Detailed exploit sequences and private implementation locations are intentionally excluded from the public brief.

## PRE-D3 relationship

RAL is currently evaluated inside Rudis's PRE-D3 campaign.

The public objective is to demonstrate, on a controlled candidate:

```text
ONE SOVEREIGN STATE
+ MULTIPLE CONTROLLED CLIENTS
+ ONE CAUSAL AUTHORITY PATH
+ RESTART / RECOVERY
+ FAIL-CLOSED BOUNDARIES
+ REPRODUCIBLE BUILD
+ INDEPENDENT ATTACK
+ NO REAL CUSTOMERS
+ NO REAL MONEY
+ NO PRODUCTION
```

Even if those properties are demonstrated, D3 still requires a separate competent authorization.

## External review model

External reviewers should be able to examine progressively deeper evidence while preserving minimum necessary disclosure:

```text
PUBLIC ARCHITECTURE
    -> SANITIZED EVIDENCE
    -> NDA TECHNICAL DETAIL
    -> PURPOSE-BOUND RESTRICTED REVIEW
```

The public repository should contain enough information to understand the properties and audit conclusions, but not enough operational detail to reduce the cost of attacking unresolved vulnerabilities.

## What this brief does not claim

This brief does not claim that RAL is:

- production ready;
- formally verified as a whole;
- fully secure;
- independently accredited end-to-end;
- open for D3;
- deployed to real customers;
- handling real money.

Its role is to expose the architecture and falsifiable properties accurately while keeping private operational evidence appropriately bounded.
