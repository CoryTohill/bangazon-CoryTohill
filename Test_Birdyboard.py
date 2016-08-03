import unittest
from birdyboard import *


class TestBirdyBoard(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.birdyboard = BirdyBoard()
        self.birdyboard.create_user("Full name", "Screen Name")
        self.birdyboard.create_user("Other full name", "Other screen name")

    def test_create_user_appends_to_users_list(self):
        self.assertEqual(self.birdyboard.users[0].full_name, "Full name")
        self.assertEqual(self.birdyboard.users[1].screen_name, "Other screen name")

    def test_create_new_chirp_appends_to_chirps_list(self):
        self.birdyboard.create_chirp("Hello", "abc123")

        self.assertEqual(self.birdyboard.chirps[0].message, "Hello")
        self.assertEqual(self.birdyboard.chirps[0].author, "abc123")

    def test_set_user_sets_current_user(self):
        test_user = User("Test McTest", "I'm so testy")
        self.birdyboard.set_current_user(test_user)
        self.assertEqual(self.birdyboard.current_user, test_user)

    def test_conversation_dict_exists(self):
        self.assertIsNotNone(self.birdyboard.conversations)


if __name__ == '__main__':
    unittest.main()
