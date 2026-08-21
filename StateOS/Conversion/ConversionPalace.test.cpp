#include "ConversionPalace.h"

#include <cassert>

using namespace Rudis::Conversion;

int main() {
    ConversionPalace palace;

    WealthEvidence evidence{
        .evidence_id = "evidence-001",
        .subject_id = "entity-001",
        .evidence_type = "verified_work",
        .provenance_hash = "sha256:example",
        .reference_value_minor = 100000,
        .reference_currency = "EUR",
        .verified = true,
    };

    ConversionPolicy policy = palace.GetPolicy();
    policy.management_fee_ppm = 10000;          // 1%
    policy.activity_contribution_ppm = 5000;    // 0.5%
    policy.evolutionary_cost_ppm = 15000;       // 1.5%
    palace.SetPolicy(policy);

    ConversionRequest request{
        .request_id = "req-001",
        .subject_id = "entity-001",
        .identity_class = IdentityClass::Inhabitant,
        .mode = ExecutionMode::SimulationOnly,
        .direction_to_ru = true,
        .amount_minor = 100000,
        .currency = "EUR",
        .evidence_id = "evidence-001",
    };

    const auto [quote_state, quote] = palace.Quote(request, evidence);
    assert(quote_state == OperationState::Quoted);
    assert(quote.management_fee_minor == 1000);
    assert(quote.activity_contribution_minor == 500);
    assert(quote.evolutionary_cost_minor == 1500);
    assert(quote.net_minor == 97000);

    const auto receipt = palace.Settle(
        request, evidence, quote, "actor-001", 1724256000);
    assert(receipt.state == OperationState::Settled);
    assert(!palace.AuditEvents().empty());
    assert(palace.AuditEvents().back().previous_state_hash == "SOVEREIGN_STATE_UNTOUCHED");

    ConversionRequest invalid = request;
    invalid.request_id = "req-invalid";
    invalid.mode = ExecutionMode::Sovereign;
    const auto [invalid_state, invalid_quote] = palace.Quote(invalid, evidence);
    (void)invalid_quote;
    assert(invalid_state == OperationState::Rejected);

    return 0;
}
