import unittest
from user import *
from chirp import *


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.source = User("Source McLastname", "Sourcery")
        self.target = User("Target McLastname", "Targetron")

    def test_create_new_private_chirp(self):
        chirp = Chirp(
            message="Hey you",
            user=self.source.user_id,
            private=True,
            receiver=self.target.user_id
        )
        is_in_a_conversation = CoversationSingleton.chirp_exists_in_a_conversation(chirp)

        self.assertTrue(is_in_a_conversation)
        self.assertEqual(chirp.message, "Hey you")
        self.assertEqual(chirp.user_id, self.source.user_id)
        self.assertEqual(chirp.private, True)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)
        self.assertIsNotNone(chirp.timestamp)
        self.asserIsEqual(chirp.receiver_id, self.target.user_id)

    def test_create_reply_private_chirp(self):
        chirp = Chirp(
            message="Hey man",
            user=self.source.user_id,
            private=True,
            receiver=self.target.user_id
        )
        is_in_a_conversation = CoversationSingleton.chirp_exists_in_a_conversation(chirp)

        self.assertTrue(is_in_a_conversation)
        self.assertEqual(chirp.message, "Hey man")
        self.assertEqual(chirp.user_id, self.source.user_id)
        self.assertEqual(chirp.private, True)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)
        self.assertIsNotNone(chirp.timestamp)
        self.asserIsEqual(chirp.receiver_id, self.target.user_id)

    def test_create_new_public_chirp(self):
        chirp = Chirp(
            message="Hello all",
            user=self.source.user_id
        )
        is_in_a_conversation = CoversationSingleton.chirp_exists_in_a_conversation(chirp)
        self.assertTrue(is_in_a_conversation)
        self.assertEqual(chirp.message, "Hello all")
        self.assertEqual(chirp.user_id, self.source.user_id)
        self.assertEqual(chirp.private, False)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)
        self.assertIsNotNone(chirp.timestamp)

    def test_create_reply_public_chirp(self):
        chirp = Chirp(
            message="Hello everyone",
            user=self.source.user_id
        )
        is_in_a_conversation = CoversationSingleton.chirp_exists_in_a_conversation(chirp)

        self.assertTrue(is_in_a_conversation)
        self.assertEqual(chirp.message, "Hello everyone")
        self.assertEqual(chirp.user_id, self.source.user_id)
        self.assertEqual(chirp.private, True)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)
        self.assertIsNotNone(chirp.timestamp)


if __name__ == '__main__':
    unittest.main()
