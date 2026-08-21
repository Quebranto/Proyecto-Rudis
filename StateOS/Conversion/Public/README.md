# Public Conversion Contracts

This directory contains the non-sensitive public contract for the Rudis Conversion Palace.

It defines the collaboration boundary between the public State OS architecture and the private operational implementation.

## Public

- types and state names;
- request/quote/authorization/settlement separation;
- audit event shape;
- simulation-facing contracts;
- integration interfaces.

## Private

The repository `Quebranto/tt` contains the operational implementation, internal tests, sensitive security mechanisms, custody details and future production integrations.

No public file in this directory should contain secrets, production credentials, private keys, sensitive defensive parameters, or the detailed mechanics of RU security.

## Required lifecycle

```text
Evidence
  -> Quote
  -> Authorization
  -> Reservation
  -> Simulation/Settlement
  -> Receipt
  -> Audit
```

A missing technical service is an `IMPLEMENTATION_DEPENDENCY`, not a constitutional decision.

Simulation must never mutate sovereign state.
