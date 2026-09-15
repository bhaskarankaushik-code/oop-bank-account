# OOP Bank Account — Python + pandas

A simple OOP banking system with transaction history, paired with a
pandas-based analysis of the transaction data it produces.

## Files

| File | What it does |
|------|--------------|
| `bank_account.py` | Defines the `BankAccount` class: deposit, withdraw, print history, and save transactions to CSV |
| `analyze_transactions.py` | Reads the saved transaction data, prints summary statistics, and saves charts |
| `tests/test_file_paths.py` | Verifies the project works correctly even when scripts are launched from a different folder |

## How it works

1. `bank_account.py` creates a `BankAccount`, performs a few deposits and withdrawals,
   and saves the results to `transactions.csv` in the project directory.
2. `analyze_transactions.py` reads that CSV with pandas and prints:
   - total deposited / withdrawn
   - number of transactions
   - average and largest transaction size
   - spending grouped by label (Rent, Grocery, Netflix, etc.)
3. It also saves two charts in the project folder:
   - `transactions_chart.png`
   - `spending_by_label.png`

## Path handling

The scripts use the project folder as the base location for all output files,
so they work reliably even when run from outside the project directory.
This avoids the common bug where the code tries to read or write files in the
current terminal folder instead of the repository folder.

## Run it

```bash
pip install pandas matplotlib

python3 bank_account.py
python3 analyze_transactions.py
```

## Verify the fix

```bash
python3 -m unittest tests/test_file_paths.py
```

This confirms the file-handling behavior is working correctly.
