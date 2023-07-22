import time


class MyString(str):
    """Class MyString.
Parent Class:str
art: name, time"""
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance

    def __str__(self):
        return f'{self = } {self.name = } {self.time =}'