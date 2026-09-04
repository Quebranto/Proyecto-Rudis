# Rudis — Restricted Technical Review Protocol

**Purpose:** enable serious external technical diligence without creating unrestricted operational access.

`REVIEW RIGHTS != GOVERNANCE RIGHTS`

`ACCESS != OWNERSHIP`

`ACCESS != PUBLICATION`

## 1. Entry conditions

Restricted review requires:

1. a named reviewing organization;
2. named reviewers or an approved reviewer class;
3. a defined technical question;
4. an NDA or equivalent confidentiality basis where necessary;
5. an approved disclosure scope;
6. minimum necessary access;
7. explicit handling rules for vulnerability information;
8. a start and end condition.

## 2. Review object

A review must identify the exact object being evaluated without requiring that its sensitive locator be made public.

The internal review record should bind:

```text
EVIDENCE_HANDLE
CANDIDATE_IDENTITY
SOURCE STATE
BUILD RECIPE
ARTIFACTS
TEST SET
EXPECTED PROPERTY
KNOWN LIMITATIONS
REVIEW WINDOW
```

The public record may cite only the evidence handle and sanitized disposition.

## 3. Permitted reviewer actions

Within scope, reviewers may:

- inspect selected source;
- reproduce builds;
- run approved test harnesses;
- attempt to falsify agreed claims;
- review architecture and trust boundaries;
- report security findings;
- recommend HOLD / FAIL / remediation;
- request narrowly scoped additional evidence.

## 4. Not granted automatically

Restricted review does not grant:

- authority over Canon;
- decision rights in the Assembly;
- ownership of Rudis IP;
- commercial exclusivity;
- rights to redistribute private implementation;
- permission to publish findings with sensitive operational detail;
- access to unrelated private material;
- D3/D4/production authorization.

## 5. Vulnerability handling

For a live finding:

```text
FIND -> ACKNOWLEDGE -> CLASSIFY -> CONTAIN DISCLOSURE -> REPAIR -> RETEST -> REATTACK -> SANITIZED DISPOSITION
```

Public communication should preserve the substance of the finding while withholding exploit-enabling detail unless responsible disclosure requires otherwise.

## 6. Access minimization

Prefer, in order:

1. sanitized evidence summary;
2. bounded artifact;
3. selected file/module;
4. temporary read-only subset;
5. broader access only when the review question cannot otherwise be answered.

`FULL REPOSITORY ACCESS = EXCEPTION, NOT DEFAULT`

## 7. Independence

A reviewer may be paid or engaged by a partner and still perform a useful independent technical review, but the relationship must be disclosed in the evidence record.

A builder's own result is builder evidence, not independent accreditation.

## 8. Exit

At the end of review:

- access should be revoked or reduced;
- confidential copies handled according to agreement;
- findings preserved;
- unresolved findings remain visible at the appropriate sanitized level;
- any future access requires a new or continuing purpose.

## 9. Final rule

> External diligence should increase confidence by increasing the project's exposure to falsification, not by increasing unnecessary exposure of its operational surface.
