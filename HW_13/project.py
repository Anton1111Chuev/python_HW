'''Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта.
Класс имеет следующие методы:
Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя
и проверяет есть ли он в списке пользователей проекта.
Если в списке его нет, то вызывается исключение доступа.
 Если пользователь присутствует в списке пользователей проекта, то пользователь
 , который входит получает его уровень доступа и становится администратором.
Метод добавление пользователя в список пользователей.
 Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.
* метод удаления пользователя из списка пользователей проекта
* метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера'''
import json

from exept import UserAccessExeption, UserInitializationExeption, UserLevelExeption
from user import User


class Project:
    __NAME_USERS_FILE = 'testUsers.json'

    def __init__(self, user_ls: list = None, admin: User = None):
        self.admin = admin
        self.user_ls = user_ls

    @classmethod
    def load_json(cls):
        with (open(cls.__NAME_USERS_FILE, 'r', encoding='utf-8') as f):
            file_data = json.load(f)
        user_ls = [User(el["name"], el["id"], el["level"]) for el in file_data]
        return cls(user_ls)

    def inter_project(self, name: str, id: int):
        if self.user_ls is None:
            raise UserInitializationExeption
        user = User(name, id)
        for el in self.user_ls:
            if user == el:
                self.admin = el
                break
        else:
            raise UserAccessExeption(user)

    def add_user(self, name: str, id: int, level: int):
        self.__check_initialization()
        user = User(name, id, level)
        if user.level < self.admin.level:
            raise UserLevelExeption(self.admin)
        self.user_ls.append(user)

    def del_user(self, name: str, id: int, level: int):
        self.__check_initialization()
        user = User(name, id, level)
        if user.level < self.admin.level:
            raise UserLevelExeption(self.admin)
        self.user_ls.remove(user)

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.__NAME_USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.user_ls, f)

    def __check_initialization(self):
        if self.admin is None or self.user_ls is None:
            raise UserInitializationExeption

    def __str__(self):
        return f'{self.admin = }; {self.user_ls = }'


project = Project.load_json()
print(project)
project.inter_project('User2', 2)
project.add_user('User5', 5, 3)
print(project)
