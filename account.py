class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.transactions

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'balance': self.balance,
            'transactions': self.transactions
        }

    @classmethod
    def from_dict(cls, data):
        acc = cls(data['id'], data['name'], data['balance'])
        acc.transactions = data.get('transactions', [])
        return acc 