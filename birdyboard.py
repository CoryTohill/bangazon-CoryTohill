import uuid
from user import *
from chirp import *


class BirdyBoard():

    def __init__(self):
        self.chirps = {}
        self.users = {}
        self.current_user = None
        self.conversations = {}

    def set_current_user(self, user_id):
        self.current_user = user_id

    def create_user(self, full_name, screen_name):
        user = User(full_name, screen_name)
        self.users[user.user_id] = user
        self.set_current_user(user)

    def create_chirp(self, message, user_id, private=False, receiver_id=None, conversation_id=None):
        new_chirp = Chirp(message, user_id, private, receiver_id)
        self.chirps[new_chirp.chirp_id] = new_chirp
        if conversation_id is None:
            self.conversations[uuid.uuid4()] = [new_chirp.chirp_id]
        else:
            conversations[conversation_id].append(new_chirp.chrip_id)
