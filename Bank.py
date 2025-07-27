class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds")
        self.balance -= amount
        self.transactions.append(f"Withdrawal: -{amount}")

    def transfer(self, target_account, amount: float):
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transactions.append(f"Transfer to {target_account.account_number}: -{amount}")
        target_account.transactions.append(f"Transfer from {self.account_number}: +{amount}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number: str, initial_balance: float = 0.0):
        if account_number in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[account_number] = Account(account_number, initial_balance)
        return self.accounts[account_number]

    def get_account(self, account_number: str):
        return self.accounts.get(account_number)
