# QUEBRANTO-19 — EVIDENCE VERIFIER v0.1

**Estado:** Contrato público de infraestructura  
**Ámbito:** Gremio Conversor / Palacio de Conversión  
**Naturaleza:** verificación técnica; no concede autoridad política.

## 1. Finalidad

El Evidence Verifier verifica que una evidencia de riqueza o de procedencia presentada al Palacio de Conversión posee una atestación válida y trazable.

La verificación no equivale a autorización económica. El Verifier produce una **atestación**; la autorización corresponde a la capa competente del State OS.

## 2. Frontera de autoridad

El Verifier:

- no legisla;
- no juzga;
- no decide qué bienes o trabajos generan derechos económicos;
- no modifica el Corpus;
- no autoriza liquidaciones por sí mismo.

## 3. Contrato

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

## 4. Invariantes

Una verificación válida debe:

1. estar vinculada a la evidencia concreta;
2. identificar al verificador;
3. producir una atestación trazable;
4. ser reproducible para el mismo estado de simulación cuando el proveedor así lo permita;
5. fallar cerrado si no existe proveedor o la atestación no puede verificarse.

El campo histórico `verified` de las estructuras de compatibilidad no constituye, por sí mismo, una prueba de autenticidad.

## 5. Criptografía

En simulación puede existir un verifier determinista de pruebas, **claramente identificado como test/simulation-only**.

En producción se deberá utilizar una implementación criptográfica real, conforme a los contratos de seguridad del proyecto. Un hash simple no debe presentarse como firma, HMAC o autenticación.

## 6. Dependencias

- `IMPLEMENTATION_DEPENDENCY`: integración con el proveedor real.
- `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`: criterios normativos sobre qué tipos de evidencia son jurídicamente admisibles, cuando el Corpus aún no los haya definido.

## 7. Criterio de aceptación

Evidencia alterada, atestación ausente, verificador inexistente o atestación incompatible → **rechazo**.

El resultado debe poder enlazarse posteriormente con el Ledger y el Palacio de Tormentas.
