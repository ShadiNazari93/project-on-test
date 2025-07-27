from Bank import Account, Bank, InsufficientFundsError

deposit = Bank().create_account("123", "100")
print(deposit)