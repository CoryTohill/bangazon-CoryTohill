import unittest
from birdyboard import *


class TestBirdyBoard(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.birdyboard = BirdyBoard()
        self.birdyboard.new_user("Captain Screen Name", "Full Name")
        self.birdyboard.new_user("2nd Screen Name", "Full Second Name")

    def test_create_new_user(self):
        self.assertEqual(self.birdyboard.users[0]['screen_name'], "Captain Screen Name")
        self.assertEqual(self.birdyboard.users[0]['full_name'], "Full Name")
        self.assertTrue(self.birdyboard.users[0]['user_id'])

    def test_create_public_chirp(self):
        self.birdyboard.create_chirp("This is my chirp.", True, 2)

        self.assertEqual(self.birdyboard.chirps[0]['message'], "This is my chirp.")
        self.assertTrue(self.birdyboard.chirps[0]['is_private'])
        self.assertEqual(self.birdyboard.chirps[0]['author'], self.birdyboard.users[1]['user_id'])
        self.assertTrue(self.birdyboard.chirps[0]['chirp_id'])
        self.assertEqual(self.birdyboard.chirps[0]['chirped_at_user'], 2)

    def test_reply_message_added_to_chirp(self):
        self.birdyboard.reply_to_chirp("This is a reply.", 1)

        self.assertEqual(self.birdyboard.chirps[0].replies[0], "This is a reply.")


if __name__ == '__main__':
    unittest.main()
