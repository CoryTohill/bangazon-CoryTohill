import unittest
from user import *


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def test_new_user_creation(self):
        user = User("Firstname McLastname", "Dude")
        self.assertEqual(user.full_name, "Firstname McLastname")
        self.assertEqual(user.screen_name, "Dude")
        self.assertIsNotNone(user.user_id)
        self.assertIsInstance(user, User)

if __name__ == '__main__':
    unittest.main()
