import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(initial_balance=100)
        self.account2 = Account(initial_balance=0)
    
    def test_withdraw_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
    
    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_deposit_success(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-20)

    def test_transferMoney_success(self):
        self.account.transferAmount(100, self.account2)
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(self.account2.balance, 100)

    def test_transferMoney_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.transferAmount(200, self.account2)
    
    def test_transferMoney_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.transferAmount(-20, self.account2)

if __name__ == '__main__':
    unittest.main()
