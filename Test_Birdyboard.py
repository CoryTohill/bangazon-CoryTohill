import unittest
from birdyboard import *
import birdyboard_menu


class TestBirdyBoard(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.birdyboard = BirdyBoard()
        self.birdyboard.new_user("Captain Screen Name", "Full Name")
        self.birdyboard.new_user("2nd Screen Name", "Full Second Name")
        self.menu = birdyboard_menu.BirdyBoardMenu()

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
        self.birdyboard.reply_to_chirp("This is a reply.", '12345')

        self.assertEqual(self.birdyboard.replies[0]['message'], "This is a reply.")
        self.assertEqual(self.birdyboard.replies[0]['chirp_id'], '12345')

    def test_set_user_sets_current_user(self):
        self.birdyboard.set_current_user("this_is_a_test_id")
        self.assertEqual(self.birdyboard.current_user, "this_is_a_test_id")

    def test_BirdyBoard_instance_created_in_menu(self):
        self.assertIsInstance(self.menu.board, BirdyBoard)

if __name__ == '__main__':
    unittest.main()
