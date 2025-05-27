import unittest
from app.cli import create_account, deposit_funds, withdraw_funds
from app.database import session
from app.models import User

class TestBankingApp(unittest.TestCase):

    def setUp(self):
        self.user = User(username='testuser', balance=0)
        session.add(self.user)
        session.commit()

    def tearDown(self):
        session.query(User).filter_by(username='testuser').delete()
        session.commit()

    def test_create_account(self):
        account = create_account('newuser', 100)
        self.assertEqual(account.username, 'newuser')
        self.assertEqual(account.balance, 100)

    def test_deposit_funds(self):
        deposit_funds(self.user.username, 50)
        updated_user = session.query(User).filter_by(username=self.user.username).first()
        self.assertEqual(updated_user.balance, 50)

    def test_withdraw_funds(self):
        deposit_funds(self.user.username, 100)
        withdraw_funds(self.user.username, 50)
        updated_user = session.query(User).filter_by(username=self.user.username).first()
        self.assertEqual(updated_user.balance, 50)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            withdraw_funds(self.user.username, 100)

if __name__ == '__main__':
    unittest.main()