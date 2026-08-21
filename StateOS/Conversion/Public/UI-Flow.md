# Public UI Flow — Palacio de Conversión

The public UI contract exposes state transitions without exposing sensitive security implementation.

```text
REQUEST
  -> IDENTITY
  -> EVIDENCE
  -> QUOTE
  -> AUTHORIZATION
  -> RESERVATION
  -> SETTLEMENT / SIMULATION
  -> RECEIPT
  -> AUDIT
```

## Rules

The UI is a projection of State OS state; it does not create authority.

The user must be able to distinguish:

- `SIMULATION_ONLY`;
- `IMPLEMENTATION_DEPENDENCY`;
- `CONSTITUTIONAL_AUTHORIZATION_REQUIRED`;
- `REJECTED`;
- `SETTLED`.

The public UI must not reveal private keys, custody topology, sensitive anti-fraud controls, or production financial integrations.

The Conversion Palace remains an executor of current policy, not a legislative authority.
