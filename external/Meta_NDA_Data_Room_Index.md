# Rudis — Meta NDA Data Room Index

**Purpose:** define what may be disclosed during structured diligence without defaulting to unrestricted private-repository access.

`NDA != UNLIMITED ACCESS`

`DUE DILIGENCE -> PURPOSE-BOUND DISCLOSURE`

## Room 0 — Public baseline

Available without NDA:

- public repository;
- Rudis public one-pager;
- RAL Public Architecture Brief;
- Maturity & Limits Statement;
- Sanitized Security Posture;
- Disclosure Classification Matrix;
- public Canon / architecture / decisions;
- public IP/license/provenance summary.

## Room 1 — Corporate / legal diligence

NDA required where non-public detail is included.

- identity of contracting party / proposed vehicle;
- founder rights and asset map;
- contributor-rights register;
- material third-party licenses;
- trademark / brand status;
- proposed licensing model;
- material contractual restrictions;
- tax / regulatory diligence status;
- insurance status where applicable.

No personal documents should be disclosed beyond what is necessary for a legitimate diligence purpose.

## Room 2 — Technical architecture

- detailed RAL / StateOS architecture;
- trust-boundary map;
- authority-chain contracts;
- client / Unreal / agent boundaries;
- continuity and recovery architecture;
- selected schemas / interfaces;
- threat-model summary;
- environment and dependency inventory at the minimum necessary level.

## Room 3 — Evidence and reproducibility

- selected test summaries;
- independent-review dispositions;
- reproducibility recipe at appropriate disclosure level;
- artifact provenance summary;
- controlled evidence handles;
- known FAIL / HOLD / residual-risk register;
- build/package evidence sufficient for the stated diligence question.

## Room 4 — Security diligence

Restricted NDA / named reviewers.

- detailed closed-finding history where useful;
- current residual risks;
- vulnerability remediation evidence;
- selected redacted logs;
- dependency / supply-chain review;
- access-control and secret-management posture;
- incident-response assumptions.

Open exploit recipes and unnecessary internal topology remain excluded by default.

## Room 5 — Restricted candidate review

Only after explicit technical scope and named reviewers:

- exact PRE-D3 candidate identity;
- selected private source necessary for the review;
- exact reproducibility artifacts;
- selected test harnesses;
- detailed evidence required to falsify a specific claim;
- vulnerability information under responsible-disclosure controls.

This room is not equivalent to a full clone of the private Forge.

## Room 6 — Commercial / financial diligence

- financing proposal;
- staged budget;
- use-of-funds policy;
- founder discretionary allocation framework;
- milestone / tranche structure;
- commercial model;
- hiring / contractor plan;
- runway scenarios;
- strategic partnership rights proposed;
- investor/partner reserved matters proposed;
- explicit list of rights not transferred by financing.

## Access log

Each non-public disclosure should record:

```text
RECIPIENT
ORGANIZATION
DATE
PURPOSE
NDA / LEGAL BASIS
ROOM / DOCUMENT
CLASSIFICATION
ACCESS DURATION
RESTRICTIONS
WITHDRAWAL / DELETION REQUEST STATUS
OWNER OF APPROVAL
```

## Release principle

`SHOW THE MINIMUM THAT ANSWERS THE DILIGENCE QUESTION`

Do not disclose a higher room because a lower room produced interest.
