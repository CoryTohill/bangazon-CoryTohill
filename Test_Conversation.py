import unittest
from conversation import *
from birdyboard import *

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.source = User("Jeff Everyman", "Jeffy")
        self.chirp = Chirp("Hello people", source.user_id)

    def test_create_new_conversation(self):
        conversation = Conversation(self.chirp)

        self.assertIsNotNone(conversation.conversation_id)
        self.assertEqual(conversation[conversation_id][0], self.chirp.chirp_id)


if __name__ == '__main__':
    unittest.main()
