import copy
import json
import unittest
from pathlib import Path

from validate_campaign import ManifestError, validate


MANIFEST = Path(__file__).with_name("campaign-manifest-v0.1.json")


class CampaignManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def reject(self, mutate) -> None:
        candidate = copy.deepcopy(self.data)
        mutate(candidate)
        with self.assertRaises(ManifestError):
            validate(candidate)

    def test_sealed_manifest_is_valid(self) -> None:
        validate(self.data)

    def test_snapshot_substitution_is_rejected(self) -> None:
        self.reject(lambda d: d["entries"][0].update(commit="main"))

    def test_duplicate_identity_is_rejected(self) -> None:
        self.reject(lambda d: d["entries"][1].update(id=d["entries"][0]["id"]))

    def test_duplicate_repository_is_rejected(self) -> None:
        self.reject(lambda d: d["entries"][1].update(repository=d["entries"][0]["repository"]))

    def test_phase_escalation_is_rejected(self) -> None:
        self.reject(lambda d: d.update(maximum_phase="D3"))

    def test_runtime_network_is_rejected(self) -> None:
        self.reject(lambda d: d.update(runtime_network_allowed=True))

    def test_direct_kernel_route_is_rejected(self) -> None:
        self.reject(lambda d: d["integration_boundary"].update(allowed_ingress=["SovereignKernel"]))

    def test_removed_sovereign_boundary_is_rejected(self) -> None:
        self.reject(lambda d: d["integration_boundary"]["forbidden_direct_consumers"].remove("ContinuityLedger"))

    def test_conformance_authority_inflation_is_rejected(self) -> None:
        self.reject(lambda d: d["integration_boundary"].update(external_conformance_grants_authority=True))

    def test_consent_mandate_inflation_is_rejected(self) -> None:
        self.reject(lambda d: d["integration_boundary"].update(technical_consent_is_juridical_mandate=True))


if __name__ == "__main__":
    unittest.main()

