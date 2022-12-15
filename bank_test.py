import unittest

from bank import Bank, BankAccount

class TestBank(unittest.TestCase):
    def test_add_account(self):
        # create a Bank instance
        bank = Bank()

        # create a BankAccount and add it to the Bank
        account = BankAccount("John Doe", "123456", "password", 1000)
        bank.add_account(account)

        # check if the BankAccount is added to the Bank
        self.assertIn(account, bank.accounts.values())

    def test_get_account(self):
        # create a Bank instance
        bank = Bank()

        # create a BankAccount and add it to the Bank
        account = BankAccount("John Doe", "123456", "password", 1000)
        bank.add_account(account)

        # get the BankAccount from the Bank
        result = bank.get_account("123456")

        # check if the returned BankAccount is the same as the added BankAccount
        self.assertEqual(account, result)

    def test_process_request(self):
        # create a Bank instance
        bank = Bank()

        # create a BankAccount and add it to the Bank
        account = BankAccount("John Doe", "123456", "password", 1000)
        bank.add_account(account)

        # add a withdrawal request to the queue
        bank.requests.put((account, "withdraw", 500, 500))

        # process the request in the queue
        bank.process_request((account, "withdraw", 500, 500))

        # check if the BankAccount balance is updated
        self.assertEqual(account.initial_balance, 500)

        # add a deposit request to the queue
        bank.requests.put((account, "deposit", 1000, 1500))

        # process the request in the queue
        bank.process_request((account, "deposit", 1000, 1500))

        # check if the BankAccount balance is updated
        self.assertEqual(account.initial_balance, 1500)

    def test_process_requests(self):
        # create a Bank instance
        bank = Bank()

        # create a BankAccount and add it to the Bank
        account = BankAccount("John Doe", "123456", "password", 1000)
        bank.add_account(account)

        # add withdrawal and deposit requests to the queue
        bank.requests.put((account, "withdraw", 500, 500))
        bank.requests.put((account, "deposit", 1000, 1500))

        # process the requests in the queue
        bank.process_requests()

        # check if the BankAccount balance is updated
        self.assertEqual(account.initial_balance, 1500)

    def test_withdraw(self):
        # create a Bank instance
        bank = Bank()

        # create a BankAccount and add it to the Bank
        account = BankAccount("John Doe", "123456", "password", 1000)
        bank.add_account(account)

        # withdraw money from the account
        bank.withdraw("123456", 500)

        # check if the BankAccount balance is updated
        self.assertEqual(account.initial_balance, 500)

        # check if the request is added to the queue
        self.assertEqual(bank.requests.get(), ("123
        

