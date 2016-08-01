import uuid


class BirdyBoard():

    def __init__(self):
        self.chirps = []
        self.users = []
        self.current_user = None
        self.replies = []

    def set_current_user(self, user_id):
        self.current_user = user_id

    def new_user(self, screen_name, full_name):
        user = {
            'screen_name': screen_name,
            'full_name': full_name,
            'user_id': uuid.uuid4()
        }
        self.users.append(user)
        self.set_current_user(user['user_id'])

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
        reply = {
            'message': message,
            'chirp_id': chirp_id
        }
        self.replies.append(reply)
