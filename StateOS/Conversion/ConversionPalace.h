#pragma once

#include <cstdint>
#include <optional>
#include <string>
#include <utility>
#include <vector>

namespace Rudis::Conversion {

enum class ExecutionMode {
    Sovereign,
    SimulationOnly,
};

enum class IdentityClass {
    Visitor,
    Inhabitant,
    Citizen,
    ExternalActor,
};

enum class OperationState {
    Quoted,
    Authorized,
    Settling,
    Settled,
    Rejected,
    Expired,
    Disputed,
    Reversed,
};

enum class PolicyState {
    TechnicalImplementationAllowed,
    ImplementationDependency,
    UnresolvedConstitutionalDependency,
    ConstitutionalAuthorizationRequired,
};

struct WealthEvidence {
    std::string evidence_id;
    std::string subject_id;
    std::string evidence_type;
    std::string provenance_hash;
    std::int64_t reference_value_minor = 0;
    std::string reference_currency = "EUR";
    bool verified = false;
};

struct ConversionPolicy {
    std::string policy_id;
    std::uint64_t version = 0;
    std::int64_t ru_per_eur_ppm = 0;          // 1 RU = ? EUR, expressed deterministically.
    std::int64_t management_fee_ppm = 0;
    std::int64_t activity_contribution_ppm = 0;
    std::int64_t evolutionary_cost_ppm = 0;
    bool allow_external_conversion = false;
    bool allow_credit = false;
    PolicyState state = PolicyState::ImplementationDependency;
};

struct ConversionRequest {
    std::string request_id;
    std::string subject_id;
    IdentityClass identity_class = IdentityClass::Visitor;
    ExecutionMode mode = ExecutionMode::SimulationOnly;
    bool direction_to_ru = true;
    std::int64_t amount_minor = 0;
    std::string currency = "EUR";
    std::string evidence_id;
};

struct ConversionQuote {
    std::string quote_id;
    std::string request_id;
    std::uint64_t policy_version = 0;
    std::int64_t gross_minor = 0;
    std::int64_t management_fee_minor = 0;
    std::int64_t activity_contribution_minor = 0;
    std::int64_t evolutionary_cost_minor = 0;
    std::int64_t net_minor = 0;
    std::string settlement_currency = "RU";
    bool deterministic = true;
};

struct ConversionReceipt {
    std::string receipt_id;
    std::string request_id;
    OperationState state = OperationState::Rejected;
    std::string policy_id;
    std::uint64_t policy_version = 0;
    std::string evidence_hash;
    std::string state_hash;
    std::string audit_event_id;
};

struct RUAsset {
    std::string asset_id;
    std::string issuer_identity;
    std::string owner_identity;
    std::int64_t amount_minor = 0;
    std::string provenance_hash;
    std::optional<std::string> message_commitment;
    bool authentic = false;
};

struct TreasuryState {
    std::int64_t ru_liquidity_minor = 0;
    std::int64_t external_liquidity_minor = 0;
    std::int64_t sovereign_fund_minor = 0;
    std::uint64_t policy_version = 0;
};

struct ConversionAuditEvent {
    std::string event_id;
    std::string request_id;
    std::string actor_id;
    std::string action;
    std::string reason;
    std::string previous_state_hash;
    std::string resulting_state_hash;
    std::uint64_t timestamp = 0;
};

class ConversionPalace final {
public:
    explicit ConversionPalace(TreasuryState treasury = {});

    void SetPolicy(ConversionPolicy policy);
    [[nodiscard]] const ConversionPolicy& GetPolicy() const noexcept;
    [[nodiscard]] const TreasuryState& GetTreasury() const noexcept;

    [[nodiscard]] std::pair<bool, std::string> ValidateEvidence(
        const WealthEvidence& evidence) const;

    [[nodiscard]] std::pair<OperationState, ConversionQuote> Quote(
        const ConversionRequest& request,
        const WealthEvidence& evidence) const;

    [[nodiscard]] ConversionReceipt Settle(
        const ConversionRequest& request,
        const WealthEvidence& evidence,
        const ConversionQuote& quote,
        std::string actor_id,
        std::uint64_t timestamp);

    [[nodiscard]] const std::vector<ConversionAuditEvent>& AuditEvents() const noexcept;

    // This prototype intentionally supports simulation only until a reviewed
    // sovereign settlement backend and real custody integration are approved.
    [[nodiscard]] bool CanTouchSovereignState(
        ExecutionMode mode) const noexcept;

private:
    TreasuryState treasury_;
    ConversionPolicy policy_;
    std::vector<ConversionAuditEvent> audit_events_;
};

} // namespace Rudis::Conversion
