import uuid


class Chirp():

    def __init__(self, message, user_id, private=False, receiver_id=None):
        """ Creates an object with attributes message, author, private, receiver, and a UUID

        Method arguments:
        -----------------
        message(str) -- The message of the object
        user_id(str) -- The user UUID that will be set as the chirp's author
        private(boolean) -- Sets the private attrite to True/False, defaults to False
        receiver_id(str) -- The UUID of the user that a private chirp is sent to, defaults to None
        """
        self.message = message
        self.author = user_id
        self.private = private
        self.receiver = receiver_id
        self.chirp_id = str(uuid.uuid4())
