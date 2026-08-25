import contextlib
import io
import json
import unittest

import redacted_history_scan as scanner


class RedactedScannerTests(unittest.TestCase):
    def test_bearer_is_detected_but_never_returned(self):
        synthetic = b"ghp_" + b"A" * 32
        findings = scanner.scan_bytes(b"token=" + synthetic)
        rendered = json.dumps(findings)
        self.assertEqual(findings[0]["category"], "github-bearer")
        self.assertNotIn(synthetic.decode(), rendered)
        self.assertRegex(findings[0]["alias"], r"^EVD-[0-9a-f]{16}$")

    def test_private_locator_is_only_a_public_boundary_finding(self):
        locator = b"https://github.com/example/non-public"
        normalized = b"github.com/example/non-public"
        alias = scanner.alias_for("private-locator", normalized)
        self.assertEqual(scanner.scan_bytes(locator), [])
        findings = scanner.scan_bytes(
            locator,
            public_boundary=True,
            forbidden_locator_aliases={alias},
        )
        self.assertEqual(findings[0]["category"], "private-locator")
        self.assertNotIn(locator.decode(), json.dumps(findings))

    def test_private_key_header_is_redacted(self):
        material = b"-----BEGIN PRIVATE KEY-----\nnot-a-real-key"
        findings = scanner.scan_bytes(material)
        self.assertEqual(findings[0]["category"], "private-key")
        self.assertNotIn("BEGIN PRIVATE KEY", json.dumps(findings))


if __name__ == "__main__":
    unittest.main()

