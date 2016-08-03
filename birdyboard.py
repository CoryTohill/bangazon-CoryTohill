from user import *
from chirp import *


class BirdyBoard():

    def __init__(self):
        pass

    def new_user(self, screen_name, full_name):
        user = User()
        self.users.append(user)
        self.set_current_user(user)

    def set_current_user(self, user_id):
        self.current_user = user_id

# import uuid


# class BirdyBoard():

#     def __init__(self):
#         self.chirps = []
#         self.users = []
#         self.current_user = None
#         self.replies = []



#     def create_chirp(self, message, is_private, chirped_at_user_id):
#         chirp = {
#             'message': message,
#             'is_private': is_private,
#             'chirped_at_user_id': chirped_at_user_id,
#             'chirp_id': uuid.uuid4(),
#             'author': self.current_user['user_id']
#         }
#         self.chirps.append(chirp)

#     def reply_to_chirp(self, message, chirp_id):
#         reply = {
#             'message': message,
#             'chirp_id': chirp_id
#         }
#         self.replies.append(reply)
