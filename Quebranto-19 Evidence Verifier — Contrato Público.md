# QUEBRANTO-19 — EVIDENCE VERIFIER v0.1

**Estado:** Contrato público de infraestructura  
**Ámbito:** Gremio Conversor / Palacio de Conversión  
**Naturaleza:** verificación técnica; no concede autoridad política.

## Finalidad

El Evidence Verifier verifica que una evidencia presentada al Palacio de Conversión posee una atestación válida y trazable.

La verificación no equivale a autorización económica. El Verifier produce una atestación; la autorización corresponde a la capa competente del State OS.

## Frontera de autoridad

El Verifier no legisla, no juzga, no decide qué bienes o trabajos generan derechos económicos, no modifica el Corpus y no autoriza liquidaciones por sí mismo.

## Contrato

```cpp
struct EvidenceVerification {
    EvidenceVerificationState state;
    std::string verifier_id;
    std::string attestation_hash;
};

class EvidenceVerifier {
public:
    virtual ~EvidenceVerifier() = default;
    virtual EvidenceVerification Verify(
        const WealthEvidence& evidence) const = 0;
};
```

## Invariantes

1. La atestación debe estar vinculada a la evidencia concreta.
2. Debe identificar al verificador.
3. Debe producir una atestación trazable.
4. Debe ser reproducible para el mismo estado de simulación cuando el proveedor lo permita.
5. Debe fallar cerrado si no existe proveedor o la atestación no puede verificarse.

El campo histórico `verified` no constituye por sí mismo una prueba de autenticidad.

## Criptografía

En simulación puede existir un verifier determinista de pruebas, identificado explícitamente como `TEST`/`SIMULATION_ONLY`. En producción deberá utilizar una implementación criptográfica real conforme a los contratos de seguridad del proyecto.

Un hash simple nunca debe presentarse como firma, HMAC o autenticación.

## Dependencias

- `IMPLEMENTATION_DEPENDENCY`: integración con el proveedor real.
- `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`: criterios normativos sobre qué tipos de evidencia son jurídicamente admisibles, cuando el Corpus aún no los haya definido.

## Criterio de aceptación

Evidencia alterada, atestación ausente, verificador inexistente o atestación incompatible → **rechazo**.
