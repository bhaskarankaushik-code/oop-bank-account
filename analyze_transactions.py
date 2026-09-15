from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent
CSV_PATH = PROJECT_ROOT / "transactions.csv"

if not CSV_PATH.exists():
    raise FileNotFoundError(f"Transaction data not found at {CSV_PATH}")

df = pd.read_csv(CSV_PATH)

print("All transactions:")
print(df)

total_deposits = df[df["Type"] == "Deposit"]["Amount"].sum()
total_withdrawals = df[df["Type"] == "Withdrawal"]["Amount"].sum()

print(f"\nTotal deposited:    {total_deposits:.2f}")
print(f"Total withdrawn:    {abs(total_withdrawals):.2f}")
print(f"Number of transactions: {len(df)}")
print(f"Average transaction amount: {df['Amount'].abs().mean():.2f}")
print(f"Largest transaction: {df['Amount'].abs().max():.2f}")

# spending grouped by label (e.g. Rent, Grocery, Netflix)
spending = df[df["Type"] == "Withdrawal"].copy()
spending["Amount"] = spending["Amount"].abs()
by_label = spending.groupby("Label")["Amount"].sum().sort_values(ascending=False)

print("\nSpending by label:")
print(by_label)

# chart 1: amount per transaction
df["Amount"].plot(kind="bar", title="Transaction Amounts")
plt.xlabel("Transaction #")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig(PROJECT_ROOT / "transactions_chart.png")
plt.close()

# chart 2: spending by label
by_label.plot(kind="bar", title="Spending by Label", color="orange")
plt.xlabel("Label")
plt.ylabel("Total spent")
plt.tight_layout()
plt.savefig(PROJECT_ROOT / "spending_by_label.png")
plt.close()

print(f"\nSaved charts: {PROJECT_ROOT / 'transactions_chart.png'}, {PROJECT_ROOT / 'spending_by_label.png'}")
