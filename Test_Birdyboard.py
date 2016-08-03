import unittest
from birdyboard import *



class TestBirdyBoard(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.birdyboard = BirdyBoard()
        self.user1 = birdyboard.new_user("Full name", "Screen Name")
        self.user2 = birdyboard.new_user("Other full name", "Other screen name")

    def test_create_new_user_appends_to_users_list(self):
        self.assertEqual(self.birdyboard.users[0], self.user1)
        self.assertEqual(self.birdyboard.users[1], self.user2)

    def test_create_new_chirp_appends_to_chirps_list(self):
        chirp1 = self.birdyboard.new_chirp("Hello", self.user1.user_id)

        self.assertEqual(self.birdyboard.chirps[0], chirp1)

    def test_set_user_sets_current_user(self):
        self.birdyboard.set_current_user(self.user1)
        self.assertEqual(self.birdyboard.current_user, self.user1)

    def test_conversation_dict_exists(self):
        self.assertIsNotNone(self.birdyboard.conversations)


if __name__ == '__main__':
    unittest.main()
