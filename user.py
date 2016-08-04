import uuid


class User():

    def __init__(self, full_name, screen_name):
        """ Creates an object with attributes full_name, screen_name, and a UUID

        Method arguments:
        -----------------
        full_name(str) -- What the new user's full_name attribute will be
        screen_name(str) -- What the new user's screen_name attribute will be
        """
        self.full_name = full_name
        self.screen_name = screen_name
        self.user_id = str(uuid.uuid4())
