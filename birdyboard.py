import uuid
import pickle
from user import *
from chirp import *


class BirdyBoard():

    def __init__(self):
        self.deserialize()
        self.current_user = None
        self.conversations = {}

    def set_current_user(self, user):
        """ Sets the current_user to a new value

        Method arguments:
        -----------------
        user(obj) -- The object that will be set as the current_user
        """
        self.current_user = user

    def create_user(self, full_name, screen_name):
        """ Creates a new user,
        sets the current_user to be the new user,
        adds the new user data to the self.users dictionary using the new user's UUID as a key,
        and serializes the self.users dictionary

        Method arguments:
        -----------------
        full_name(str) -- What the new user's full_name attribute will be
        screen_name(str) -- What the new user's screen_name attribute will be
        """
        user = User(full_name, screen_name)
        self.users[user.user_id] = user
        self.set_current_user(user)
        self.serialize('users.txt', self.users)

    def create_chirp(self, message, user_id, private=False, receiver_id=None, conversation_id=None):
        """ Creates a new chirp,
        adds chirp to the self.chirps dictionary using it's UUID as a key,
        adds chirp's UUID to a conversation or creates a new conversation and then adds the UUID,
        serializes the self.chirps dictionary,
        serializes the conversations dictionary

        Method arguments:
        -----------------
        message(str) -- The message of the chirp
        user_id(str) -- The user UUID that will be set as the chirp's author
        private(boolean) -- Sets the private attrite to True/False, defaults to False
        receiver_id(str) -- The UUID of the user that a private chirp is sent to, defaults to None
        conversation_id(str) -- The conversation UUID to determine what conversation the chirp belongs to, defaults to None
        """
        new_chirp = Chirp(message, user_id, private, receiver_id)
        self.chirps[new_chirp.chirp_id] = new_chirp

        # creates a new conversation if no conversation_id is passed in
        # and with it's own UUID as the key
        # and the chirp's UUID as the first item in the value's list
        if conversation_id is None:
            self.conversations[uuid.uuid4()] = [new_chirp.chirp_id]

        # appends the chirp's UUID to an existing conversation's list of chirp ids
        else:
            self.conversations[conversation_id].append(new_chirp.chirp_id)

        self.serialize('chirps.txt', self.chirps)
        self.serialize('conversations.txt', self.conversations)

    def serialize(self, file_name, data):
        """ Serializes data to a file

        Method arguments:
        -----------------
        file_name(str) -- The file name that will be serialized to
        data(obj) -- The data to be serialized
        """
        with open(file_name, 'wb+') as f:
            pickle.dump(data, f)

    def deserialize(self):
        """ Deserializes chirps.txt, users.txt, and conversations.txt,
        and sets the self.chirps, self.users.txt and self.conversations attributes to the data respectively.
        If an error occurs desirializing any of the files, the attribute value will be set to an empty dictionary

        Method arguments:
        -----------------
        n/a
        """
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
