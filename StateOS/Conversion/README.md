# Conversion Palace — State OS Prototype

This directory contains the first portable prototype of the Rudis Conversion Palace.

## Scope

The prototype implements deterministic domain objects and a simulation-only settlement flow for:

- verified wealth evidence;
- conversion policies;
- RU/fiat quotes;
- separated management/activity/evolutionary costs;
- conversion receipts;
- audit events;
- treasury state;
- simulation isolation.

## Intentionally not implemented

This first slice does **not**:

- connect to banks;
- move real money;
- custody production keys;
- issue sovereign RU into a production ledger;
- call external FX providers;
- decide constitutional policy;
- provide regulated financial services.

## Integration boundary

The prototype is intentionally portable and isolated from the current game engine. The Cartographer and Dōng should integrate it with the State OS `Economic Core` and `Guild Runtime` only after the API contracts are agreed and Palace Observatory audit hooks are connected.

## Required invariants

1. Same input + same policy version + same evidence => same quote.
2. Simulation cannot mutate sovereign state.
3. Every settlement produces an audit event.
4. Policy parameters are versioned rather than hardcoded as political law.
5. Real-money settlement remains disabled until a separate production authorization exists.
