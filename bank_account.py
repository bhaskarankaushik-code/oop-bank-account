import csv
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []   # list of (date, type, label, amount, balance)

    def deposit(self, amount, label="Deposit"):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self._add_transaction("Deposit", label, amount)

    def withdraw(self, amount, label="Withdrawal"):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        self._add_transaction("Withdrawal", label, -amount)

    def _add_transaction(self, txn_type, label, amount):
        date = datetime.now().strftime("%Y-%m-%d")
        self.transactions.append((date, txn_type, label, amount, self.balance))

    def show_history(self):
        print(f"\nTransaction history for {self.owner}")
        print("-" * 60)
        for date, txn_type, label, amount, balance in self.transactions:
            print(f"{date}  {txn_type:<10} {label:<12} {amount:>10.2f}   Balance: {balance:.2f}")
        print("-" * 60)
        print(f"Current balance: {self.balance:.2f}\n")

    def save_to_csv(self, filename="transactions.csv"):
        target_path = PROJECT_ROOT / filename
        with open(target_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Type", "Label", "Amount", "Balance"])
            writer.writerows(self.transactions)
        print(f"Saved transactions to {target_path}")


# ---- demo ----
if __name__ == "__main__":
    account = BankAccount("Kaushik", balance=1000)

    account.deposit(45000, "Salary")
    account.withdraw(500, "Rent")
    account.withdraw(80, "Grocery")
    account.deposit(1500, "Freelance")
    account.withdraw(200, "Grocery")
    account.withdraw(15, "Netflix")
    account.withdraw(1000000, "Car")   # will fail, not enough balance

    account.show_history()
    account.save_to_csv("transactions.csv")
