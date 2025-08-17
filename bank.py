import json
from account import Account

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, start_balance=0):
        new_id = 1 if not self.accounts else self.accounts[-1].id + 1
        account = Account(new_id, name, start_balance)
        self.accounts.append(account)
        return account

    def find_account_by_id(self, acc_id):
        for acc in self.accounts:
            if acc.id == acc_id:
                return acc
        return None

    def deposit_to_account(self, acc_id, amount):
        acc = self.find_account_by_id(acc_id)
        if not acc:
            raise ValueError("Account not found.")
        acc.deposit(amount)

    def withdraw_from_account(self, acc_id, amount):
        acc = self.find_account_by_id(acc_id)
        if not acc:
            raise ValueError("Account not found.")
        acc.withdraw(amount)

    def show_account_details(self, acc_id):
        acc = self.find_account_by_id(acc_id)
        if not acc:
            raise ValueError("Account not found.")
        return {
            'id': acc.id,
            'name': acc.name,
            'balance': acc.get_balance(),
            'transactions': acc.get_history()
        }

    def save_to_file(self, filename='bank.json'):
        data = [acc.to_dict() for acc in self.accounts]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename='bank.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.accounts = [Account.from_dict(acc) for acc in data]
        except FileNotFoundError:
            self.accounts = [] 