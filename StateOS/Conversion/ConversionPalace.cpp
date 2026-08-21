#include "ConversionPalace.h"

#include <algorithm>
#include <limits>

namespace Rudis::Conversion {
namespace {

std::int64_t SafeMulPpm(std::int64_t value, std::int64_t ppm) {
    if (value <= 0 || ppm <= 0) return 0;
    const auto max = std::numeric_limits<std::int64_t>::max();
    if (value > max / ppm) return max;
    return (value * ppm) / 1'000'000;
}

std::string MakeSyntheticId(const char* prefix, std::size_t index) {
    return std::string(prefix) + "-" + std::to_string(index + 1);
}

} // namespace

ConversionPalace::ConversionPalace(TreasuryState treasury)
    : treasury_(treasury) {
    policy_.policy_id = "conversion-prototype-default";
    policy_.version = 1;
    policy_.ru_per_eur_ppm = 1'000'000; // 1 RU : 1 EUR in prototype only.
    policy_.state = PolicyState::ImplementationDependency;
}

void ConversionPalace::SetPolicy(ConversionPolicy policy) {
    policy_ = std::move(policy);
}

const ConversionPolicy& ConversionPalace::GetPolicy() const noexcept {
    return policy_;
}

const TreasuryState& ConversionPalace::GetTreasury() const noexcept {
    return treasury_;
}

std::pair<bool, std::string> ConversionPalace::ValidateEvidence(
    const WealthEvidence& evidence) const {
    if (evidence.evidence_id.empty()) return {false, "missing_evidence_id"};
    if (evidence.subject_id.empty()) return {false, "missing_subject_id"};
    if (evidence.provenance_hash.empty()) return {false, "missing_provenance_hash"};
    if (evidence.reference_value_minor <= 0) return {false, "non_positive_reference_value"};
    if (!evidence.verified) return {false, "evidence_not_verified"};
    if (evidence.reference_currency.empty()) return {false, "missing_reference_currency"};
    return {true, "verified"};
}

std::pair<OperationState, ConversionQuote> ConversionPalace::Quote(
    const ConversionRequest& request,
    const WealthEvidence& evidence) const {
    ConversionQuote quote{};
    quote.quote_id = "quote-" + request.request_id;
    quote.request_id = request.request_id;
    quote.policy_version = policy_.version;
    quote.gross_minor = request.amount_minor;
    quote.settlement_currency = request.direction_to_ru ? "RU" : request.currency;

    const auto evidence_ok = ValidateEvidence(evidence);
    if (!evidence_ok.first) {
        return {OperationState::Rejected, quote};
    }
    if (request.mode == ExecutionMode::Sovereign && !CanTouchSovereignState(request.mode)) {
        return {OperationState::Rejected, quote};
    }
    if (request.amount_minor <= 0) {
        return {OperationState::Rejected, quote};
    }
    if (policy_.state != PolicyState::TechnicalImplementationAllowed &&
        request.mode == ExecutionMode::Sovereign) {
        return {OperationState::Rejected, quote};
    }

    quote.management_fee_minor = SafeMulPpm(request.amount_minor, policy_.management_fee_ppm);
    quote.activity_contribution_minor =
        SafeMulPpm(request.amount_minor, policy_.activity_contribution_ppm);
    quote.evolutionary_cost_minor =
        SafeMulPpm(request.amount_minor, policy_.evolutionary_cost_ppm);

    const auto total_cost = quote.management_fee_minor +
                            quote.activity_contribution_minor +
                            quote.evolutionary_cost_minor;
    quote.net_minor = std::max<std::int64_t>(0, request.amount_minor - total_cost);
    return {OperationState::Quoted, quote};
}

ConversionReceipt ConversionPalace::Settle(
    const ConversionRequest& request,
    const WealthEvidence& evidence,
    const ConversionQuote& quote,
    std::string actor_id,
    std::uint64_t timestamp) {
    ConversionReceipt receipt{};
    receipt.receipt_id = "receipt-" + request.request_id;
    receipt.request_id = request.request_id;
    receipt.policy_id = policy_.policy_id;
    receipt.policy_version = policy_.version;
    receipt.audit_event_id = MakeSyntheticId("audit", audit_events_.size());
    receipt.evidence_hash = evidence.provenance_hash;

    const auto evidence_ok = ValidateEvidence(evidence);
    if (!evidence_ok.first || quote.request_id != request.request_id || quote.net_minor < 0) {
        receipt.state = OperationState::Rejected;
        return receipt;
    }

    // Real sovereign settlement is intentionally not connected in v0.1.
    // Simulation can produce deterministic receipts without mutating the
    // sovereign treasury or external financial systems.
    if (request.mode != ExecutionMode::SimulationOnly) {
        receipt.state = OperationState::Rejected;
        return receipt;
    }

    receipt.state = OperationState::Settled;
    receipt.state_hash = "SIMULATION_STATE_HASH:" + request.request_id;

    ConversionAuditEvent event{};
    event.event_id = receipt.audit_event_id;
    event.request_id = request.request_id;
    event.actor_id = std::move(actor_id);
    event.action = "SIMULATION_SETTLED";
    event.reason = "simulation_only_no_sovereign_mutation";
    event.previous_state_hash = "SOVEREIGN_STATE_UNTOUCHED";
    event.resulting_state_hash = receipt.state_hash;
    event.timestamp = timestamp;
    audit_events_.push_back(std::move(event));

    return receipt;
}

const std::vector<ConversionAuditEvent>& ConversionPalace::AuditEvents() const noexcept {
    return audit_events_;
}

bool ConversionPalace::CanTouchSovereignState(ExecutionMode mode) const noexcept {
    // v0.1 intentionally fails closed. A future sovereign backend must be
    // integrated only after the constitutional and security contracts are met.
    return mode == ExecutionMode::Sovereign &&
           policy_.state == PolicyState::TechnicalImplementationAllowed;
}

} // namespace Rudis::Conversion
