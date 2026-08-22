# QUEBRANTO-20 — CONTINUITY & LEDGER ADAPTER v0.1

**Estado:** Contrato público de infraestructura  
**Ámbito:** Palacio de Conversión / Continuity Engine / Ledger  
**Naturaleza:** persistencia y continuidad técnica; no concede autoridad política.

## Finalidad

Define el adaptador que el Palacio de Conversión utilizará para registrar transiciones y delegar la persistencia durable del estado económico.

El Palacio de Conversión no es propietario de la historia soberana. La cadena durable corresponde al Continuity Engine y el histórico económico al Ledger.

## Frontera de autoridad

El adaptador:

- no legisla;
- no decide la legitimidad política de una transición;
- no modifica el Corpus;
- no sustituye al Law Engine;
- no convierte una transición rechazada en una transición válida;
- no permite que el Palacio de Conversión mantenga una segunda historia soberana paralela.

## Contrato conceptual

```cpp
struct ContinuityRequest {
    std::string request_id;
    std::string parent_state_hash;
    std::string evidence_hash;
    std::string policy_id;
    std::uint64_t policy_version;
    std::int64_t amount_origin_minor;
    std::int64_t amount_dest_minor;
    std::string actor_id;
    std::uint64_t timestamp;
    std::string simulation_id;
};

struct ContinuityResponse {
    bool accepted;
    std::string resulting_state_hash;
    std::string ledger_entry_id;
    std::string error;
};
```

## Invariantes

1. **Anti-replay:** un `request_id` ya registrado no puede volver a aceptarse.
2. **No orfandad:** el `parent_state_hash` debe pertenecer a una cadena válida.
3. **Integridad:** el estado resultante debe depender de padre + transición.
4. **Reconstrucción:** el Ledger debe conservar los datos suficientes para reproducir la transición.
5. **Atomicidad:** una transición aceptada no puede producir un recibo de éxito sin persistencia correspondiente.
6. **Fail-closed:** una dependencia de persistencia ausente no puede producir una autorización positiva.

## Simulación y producción

En `SIMULATION_ONLY` puede utilizarse un adaptador determinista de prueba. Ese adaptador no es una persistencia soberana y no debe presentarse como tal.

La persistencia de producción requiere el componente real de Continuity/Ledger y sus controles criptográficos.

## Dependencias

- `IMPLEMENTATION_DEPENDENCY`: integración con Continuity/Ledger real.
- `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`: cuestiones normativas sobre retención, privacidad, auditoría o efectos jurídicos de los registros si el Corpus aún no las hubiera definido.

## Criterio de aceptación

Una transición con padre inexistente, `request_id` duplicado, datos incompletos o estado inconsistente → **rechazo**.
