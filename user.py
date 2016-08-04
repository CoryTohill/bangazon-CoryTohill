import uuid


class User():

    def __init__(self, full_name, screen_name):
        self.full_name = full_name
        self.screen_name = screen_name
        self.user_id = str(uuid.uuid4())
