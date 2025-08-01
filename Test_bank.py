import pytest
from Bank import Account, Bank, InsufficientFundsError


class TestAccount:
    def test_deposit(self):
        acc = Account("123")
        with pytest.raises(ValueError):
            acc.deposit(-21)
        with pytest.raises(TypeError):
            acc.deposit("-21")

    def test_withdraw_success(self):
        acc = Account("123", 100)
        acc.withdraw(50)
        assert acc.balance == 50
        with pytest.raises(ValueError):
            acc.withdraw(-21)
        with pytest.raises(InsufficientFundsError):
            acc.withdraw(155)
        with pytest.raises(TypeError):
            acc.withdraw("-21")

    def test_withdraw_insufficient_funds(self):
        acc = Account("123", 50)
        with pytest.raises(InsufficientFundsError):
            acc.withdraw(100)

    def test_transfer_between_accounts(self):
        acc1 = Account("1", 100)
        acc2 = Account("2", 50)
        acc1.transfer(acc2, 30)
        assert acc1.balance == 70
        assert acc2.balance == 80


class TestBank:
    def test_create_account(self):
        bank = Bank()
        acc = bank.create_account("123", 100)
        assert acc.balance == 100
        assert bank.get_account("123") == acc

    def test_duplicate_account(self):
        bank = Bank()
        bank.create_account("123")
        with pytest.raises(ValueError):
            bank.create_account("123")

# pytest Test_bank.py -v
