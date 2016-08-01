import uuid


class BirdyBoard():

    def __init__(self):
        self.chirps = []
        self.users = []
        self.current_user = None

    def new_user(self, screen_name, full_name):
        user = {
            'screen_name': screen_name,
            'full_name': full_name,
            'user_id': uuid.uuid4()
        }
        self.users.append(user)
        self.current_user = user

    def create_chirp(self, message, is_private, chirped_at_user):
        chirp = {
            'message': message,
            'is_private': is_private,
            'chirped_at_user': chirped_at_user,
            'chirp_id': uuid.uuid4(),
            'author': self.current_user['user_id']
        }
        self.chirps.append(chirp)

    def reply_to_chirp(self, message, chirp_id):
        pass
