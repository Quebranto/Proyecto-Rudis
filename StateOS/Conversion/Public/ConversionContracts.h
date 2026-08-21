#pragma once

#include <cstdint>
#include <optional>
#include <string>

namespace Rudis::Conversion::Public {

enum class ExecutionMode : std::uint8_t {
    Sovereign,
    SimulationOnly,
};

enum class IdentityClass : std::uint8_t {
    Visitor,
    Inhabitant,
    Citizen,
    ExternalActor,
};

enum class OperationState : std::uint8_t {
    Quoted,
    Authorized,
    Reserving,
    Settling,
    Settled,
    Rejected,
    Expired,
    Disputed,
    Reversed,
};

enum class PolicyState : std::uint8_t {
    TechnicalImplementationAllowed,
    ImplementationDependency,
    UnresolvedConstitutionalDependency,
    ConstitutionalAuthorizationRequired,
};

struct MonetaryAmount {
    std::int64_t minor = 0;
    std::string currency;
};

struct WealthEvidenceRef {
    std::string evidence_id;
    std::string subject_id;
    std::string evidence_type;
    std::string provenance_reference;
    MonetaryAmount reference_value;
    bool verified = false;
};

struct ConversionPolicyRef {
    std::string policy_id;
    std::uint64_t version = 0;
    PolicyState state = PolicyState::ImplementationDependency;
};

struct ConversionQuote {
    std::string quote_id;
    std::string request_id;
    ConversionPolicyRef policy;
    MonetaryAmount gross;
    MonetaryAmount management_cost;
    MonetaryAmount activity_cost;
    MonetaryAmount evolutionary_cost;
    MonetaryAmount net;
    std::string rate_reference;
    std::uint64_t issued_at = 0;
    std::uint64_t valid_until = 0;
};

struct ConversionRequest {
    std::string request_id;
    std::string subject_id;
    IdentityClass identity_class = IdentityClass::Visitor;
    ExecutionMode mode = ExecutionMode::SimulationOnly;
    bool direction_to_ru = true;
    MonetaryAmount source;
    std::string evidence_id;
};

struct ConversionAuthorizationRef {
    std::string authorization_id;
    std::string authority_id;
    std::string competence_reference;
    bool valid = false;
};

struct ConversionReceipt {
    std::string receipt_id;
    std::string request_id;
    OperationState state = OperationState::Rejected;
    ConversionPolicyRef policy;
    std::string evidence_reference;
    MonetaryAmount gross;
    MonetaryAmount net;
    std::string state_reference;
    std::string audit_reference;
};

struct ConversionAuditEvent {
    std::string event_id;
    std::string request_id;
    std::string quote_id;
    std::string authorization_id;
    std::string receipt_id;
    std::string policy_id;
    std::string action;
    std::string reason;
    std::string parent_state_reference;
    std::string resulting_state_reference;
    std::uint64_t timestamp = 0;
};

class IQuoteService {
public:
    virtual ~IQuoteService() = default;
    virtual ConversionQuote RequestQuote(
        const ConversionRequest& request,
        const WealthEvidenceRef& evidence) = 0;
};

class IAuthorizationService {
public:
    virtual ~IAuthorizationService() = default;
    virtual ConversionAuthorizationRef Authorize(
        const ConversionRequest& request,
        const ConversionQuote& quote) = 0;
};

class ISettlementService {
public:
    virtual ~ISettlementService() = default;
    virtual ConversionReceipt Settle(
        const ConversionRequest& request,
        const ConversionQuote& quote,
        const ConversionAuthorizationRef& authorization) = 0;
};

class IAuditSink {
public:
    virtual ~IAuditSink() = default;
    virtual void Record(const ConversionAuditEvent& event) = 0;
};

// Public contract only. The implementation of sovereign settlement,
// custody, security controls and operational infrastructure remains private.
} // namespace Rudis::Conversion::Public
