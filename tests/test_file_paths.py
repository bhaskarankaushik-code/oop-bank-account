import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


class TestFilePaths(unittest.TestCase):
    def test_bank_account_saves_to_project_directory(self):
        sys.path.insert(0, str(PROJECT_ROOT))
        import bank_account

        expected_file = PROJECT_ROOT / "transactions.csv"
        if expected_file.exists():
            expected_file.unlink()

        with tempfile.TemporaryDirectory() as tmp_dir:
            original_cwd = os.getcwd()
            try:
                os.chdir(tmp_dir)
                account = bank_account.BankAccount("Test User", 100)
                account.deposit(50, "Bonus")
                account.save_to_csv("transactions.csv")
                self.assertTrue(expected_file.exists())
                self.assertFalse((Path(tmp_dir) / "transactions.csv").exists())
            finally:
                os.chdir(original_cwd)
                if expected_file.exists():
                    expected_file.unlink()

    def test_analysis_script_runs_from_any_directory(self):
        expected_file = PROJECT_ROOT / "transactions.csv"
        if expected_file.exists():
            expected_file.unlink()

        with tempfile.TemporaryDirectory() as tmp_dir:
            script_path = PROJECT_ROOT / "bank_account.py"
            result = subprocess.run(
                [sys.executable, str(script_path)],
                cwd=tmp_dir,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(expected_file.exists())

            analysis_path = PROJECT_ROOT / "analyze_transactions.py"
            result = subprocess.run(
                [sys.executable, str(analysis_path)],
                cwd=tmp_dir,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Total deposited", result.stdout)

        if expected_file.exists():
            expected_file.unlink()


if __name__ == "__main__":
    unittest.main()
