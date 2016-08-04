import uuid
import pickle
from user import *
from chirp import *


class BirdyBoard():

    def __init__(self):
        self.deserialize()
        self.current_user = None
        self.conversations = {}

    def set_current_user(self, user_id):
        self.current_user = user_id

    def create_user(self, full_name, screen_name):
        user = User(full_name, screen_name)
        self.users[user.user_id] = user
        self.set_current_user(user)
        self.serialize('users.txt', self.users)

    def create_chirp(self, message, user_id, private=False, receiver_id=None, conversation_id=None):
        new_chirp = Chirp(message, user_id, private, receiver_id)
        self.chirps[new_chirp.chirp_id] = new_chirp
        if conversation_id is None:
            self.conversations[uuid.uuid4()] = [new_chirp.chirp_id]
        else:
            self.conversations[conversation_id].append(new_chirp.chirp_id)

        self.serialize('chirps.txt', self.chirps)
        self.serialize('conversations.txt', self.conversations)

    def serialize(self, file_name, attribute):
        with open(file_name, 'wb+') as f:
            pickle.dump(attribute, f)

    def deserialize(self):
        try:
            with open('chirps.txt', 'rb+') as f:
                self.chirps = pickle.load(f)
        except:
            self.chirps = {}

        try:
            with open('users.txt', 'rb+') as f:
                self.users = pickle.load(f)
        except:
            self.users = {}

        try:
            with open('conversations.txt', 'rb+') as f:
                self.conversations = pickle.load(f)
        except:
            self.conversations = {}
