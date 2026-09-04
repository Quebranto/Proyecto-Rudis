# Rudis — External Demo Release Checklist

## Purpose

Use this checklist before sharing screenshots, video, binaries, live demos or interactive material with an external evaluator.

A demo is evidence only for what it actually demonstrates.

`DEMO != PRODUCTION`

`VISUAL COMPLETENESS != TECHNICAL COMPLETENESS`

`UI STATE != SOVEREIGN STATE`

## 1. Scope and truthfulness

- [ ] The demo has a named scope.
- [ ] The demonstrated candidate/version is internally identifiable.
- [ ] Every visible capability is real for that candidate or clearly labelled mock/fixture/simulation.
- [ ] The demo does not imply D3 or production readiness.
- [ ] HOLD / unavailable / partial states are represented honestly.
- [ ] No narration claims more than the underlying evidence supports.

## 2. Security sanitization

- [ ] No credentials, tokens, keys or secrets are visible.
- [ ] No private repository locators are visible.
- [ ] No private branch names or hashes are visible.
- [ ] No private CI IDs/URLs are visible.
- [ ] No sensitive internal paths are visible.
- [ ] No unnecessary hosts, endpoints, account identifiers or infrastructure topology are visible.
- [ ] No exploit recipe or open-vulnerability reproduction sequence is exposed.
- [ ] Logs/console output have been reviewed before capture.
- [ ] Crash/error dialogs have been reviewed for sensitive data.

## 3. PII and provenance

- [ ] No unnecessary personal data appears on screen, in logs, fixtures or filenames.
- [ ] Any third-party assets shown have known provenance/license status.
- [ ] Attribution required by licenses is preserved.
- [ ] External logos/names are used only where appropriate and not presented as endorsement.

## 4. Authority boundaries

- [ ] The client/UI/world does not appear to create authority locally.
- [ ] If an action is demonstrated, the narrative distinguishes intent from sovereign decision.
- [ ] Receipt/effect representation is not presented as self-issued authority.
- [ ] Test or simulation support is visibly separated from production-oriented composition where relevant.

## 5. Maturity statement

The demo package should carry or link to a short statement equivalent to:

```text
PRE-D3 = ACTIVE
D3 OPEN = NO
PRODUCTION = NO
REAL CUSTOMERS = NO
REAL MONEY = NO
```

## 6. Distribution controls

- [ ] Public demo material is safe for indefinite public retention.
- [ ] NDA-only demo material is labelled and stored separately.
- [ ] Restricted-review artifacts are distributed only to named reviewers with a defined purpose.
- [ ] A less sensitive version was considered before sharing the more detailed artifact.

## 7. Release decision

Release only when:

```text
TRUTHFUL SCOPE
+ SANITIZED OUTPUT
+ NO UNNECESSARY PII
+ PROVENANCE REVIEWED
+ MATURITY NOT OVERSTATED
+ AUTHORITY BOUNDARY PRESERVED
+ PURPOSE-APPROPRIATE DISTRIBUTION
= DEMO RELEASE CANDIDATE
```

Any unresolved material question -> `HOLD DEMO RELEASE`.
