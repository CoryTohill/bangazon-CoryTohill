import unittest
from user import *
from chirp import *
from birdyboard import *


class TestChirp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.source = User("Source McLastname", "Sourcery")
        self.target = User("Target McLastname", "Targetron")

    def test_create_new_private_chirp(self):
        chirp = Chirp(
            message="Hey you",
            user_id=self.source.user_id,
            private=True,
            receiver_id=self.target.user_id
        )
        self.assertEqual(chirp.message, "Hey you")
        self.assertEqual(chirp.author, self.source.user_id)
        self.assertEqual(chirp.private, True)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)
        self.assertIsNotNone(chirp.timestamp)
        self.assertEqual(chirp.receiver, self.target.user_id)

    def test_create_reply_private_chirp(self):
        chirp = Chirp(
            message="Hey man",
            user_id=self.source.user_id,
            private=True,
            receiver_id=self.target.user_id
        )
        self.assertEqual(chirp.message, "Hey man")
        self.assertEqual(chirp.author, self.source.user_id)
        self.assertEqual(chirp.private, True)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)
        self.assertIsNotNone(chirp.timestamp)
        self.assertEqual(chirp.receiver, self.target.user_id)

    def test_create_new_public_chirp(self):
        chirp = Chirp(
            message="Hello all",
            user_id=self.source.user_id
        )
        self.assertEqual(chirp.message, "Hello all")
        self.assertEqual(chirp.author, self.source.user_id)
        self.assertEqual(chirp.private, False)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)
        self.assertIsNotNone(chirp.timestamp)

    def test_create_reply_public_chirp(self):
        chirp = Chirp(
            message="Hello everyone",
            user_id=self.source.user_id
        )
        self.assertEqual(chirp.message, "Hello everyone")
        self.assertEqual(chirp.author, self.source.user_id)
        self.assertEqual(chirp.private, False)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)
        self.assertIsNotNone(chirp.timestamp)


if __name__ == '__main__':
    unittest.main()
