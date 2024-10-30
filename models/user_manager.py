class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        return True 

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        return user is not None and user.password == password