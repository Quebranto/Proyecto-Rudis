import tempfile
import unittest
from pathlib import Path

from repository_policy_gate import audit_repository, audit_workflow


PIN = "1" * 40


class WorkflowPolicyTests(unittest.TestCase):
    def test_hardened_workflow_passes(self):
        text = f"""name: safe
on: pull_request
permissions:
  contents: read
jobs:
  check:
    steps:
      - uses: actions/checkout@{PIN}
        with:
          persist-credentials: false
"""
        self.assertEqual([], audit_workflow(text, "synthetic.yml"))

    def test_privileged_untrusted_workflow_is_rejected(self):
        text = """on: pull_request_target
jobs:
  unsafe:
    steps:
      - uses: actions/checkout@v4
      - run: echo ${{ secrets.DEMO_VALUE }}
"""
        codes = {finding.code for finding in audit_workflow(text, "synthetic.yml")}
        self.assertIn("UNTRUSTED_PRIVILEGED_TRIGGER", codes)
        self.assertIn("ACTION_NOT_PINNED", codes)
        self.assertIn("CHECKOUT_HARDENING_MISSING", codes)

    def test_repository_reports_controls_without_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            findings = audit_repository(Path(temp))
        self.assertEqual(2, len(findings))
        self.assertTrue(all(f.locator.startswith("LOC-") for f in findings))
        self.assertTrue(all("CODEOWNERS" not in f.locator for f in findings))


if __name__ == "__main__":
    unittest.main()

