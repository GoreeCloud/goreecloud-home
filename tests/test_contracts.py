from __future__ import annotations

from pathlib import Path
import json
import unittest

from goreecloud_home.availability import availability_contract
from goreecloud_home.capabilities import default_capability_registry

ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def test_capability_contract_file_matches_runtime_registry(self) -> None:
        document = json.loads((ROOT / "contracts/capabilities.v1.json").read_text())
        self.assertEqual(default_capability_registry().as_contract(), document)

    def test_availability_contract_file_matches_runtime_contract(self) -> None:
        document = json.loads((ROOT / "contracts/device-availability.v1.json").read_text())
        self.assertEqual(availability_contract(), document)


if __name__ == "__main__":
    unittest.main()
