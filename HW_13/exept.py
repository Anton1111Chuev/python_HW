from user import User

class MyExeption(Exception):
    pass


class UserLevelExeption(MyExeption):
    def __init__(self, user: User):
        self.user = user

    def __str__(self):
        return f'User: ({self.user}) has access level below required'

class UserInitializationExeption(MyExeption):
    def __str__(self):
        return f'Admin or list user is not exis'

class UserAccessExeption(MyExeption):
    def __init__(self, user:User):
        self.user = user

    def __str__(self):
        return f'User: ({self.user}) is not in list'


