import uuid
import datetime


class Chirp():

    def __init__(self, message, user_id, private=False, receiver_id=None):
        self.message = message
        self.author = user_id
        self.private = private
        self.receiver = receiver_id
        self.chirp_id = str(uuid.uuid4())
        self.timestamp = datetime.datetime.now()
