import csv

'''Создайте класс студента.
* Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
* Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
* Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
* Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.'''


class BaseDescriptor:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        pass


class RangeInt(BaseDescriptor):
    def __init__(self, min_value, max_value):
        self._max_value = max_value
        self._min_value = min_value

    def validate(self, value: int):
        if not isinstance(value, int):
            raise TypeError
        if value > self._max_value or value < self._min_value:
            raise ValueError("bad value")


class StrDescriptor(BaseDescriptor):
    def validate(self, value: str):
        if not isinstance(value, str):
            raise TypeError
        if not value.istitle() or not value.isalpha():
            raise ValueError("bad value")


class Student:
    """Class Student"""
    __NAME_CVS = "test_svs.csv"
    _name = StrDescriptor()
    _last_name = StrDescriptor
    _currect_test = RangeInt(1, 100)
    _currect_grade = RangeInt(1, 5)

    def __init__(self, name, last_name):
        self._last_name = last_name
        self._name = name
        self.__subjects = set()
        with open(self.__NAME_CVS, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                self.__subjects = set(row)
        self._testes = dict.fromkeys(self.__subjects)
        self._grades = dict.fromkeys(self.__subjects)
        # интересное поведение если передать в fromkeys пустой список будет аналогично вызову процедуры с параметром по умолчанию = [] - будет один общий список

    def __repr__(self):
        return f'{self._last_name = }; {self._name = }; {self.__subjects = }  '

    def __str__(self):
        return f'{self._last_name} {self._name}'

    @property
    def subjects(self):
        return self.__subjects

    def add_subject(self, subject: str):
        self.__subjects.add(subject)

    def __check_subject(self, value: str):
        if not isinstance(value, str):
            raise TypeError
        if value not in self.__subjects:
            raise ValueError("incorrect subject")

    def add_test(self, subject: str, test_grade: int):
        self.__add_grade(subject, test_grade, '_currect_test', '_testes')

    def add_grade(self, subject: str, grade: int):
        self.__add_grade(subject, grade, '_currect_grade', '_grades')

    def __add_grade(self, subject: str, grade: int, cur_atr_name, dict_art_name):
        self.__check_subject(subject)
        setattr(self, cur_atr_name, grade)
        dict = getattr(self, dict_art_name)
        ls = dict.setdefault(subject)
        if isinstance(ls, list):
            ls.append(grade)
        else:
            dict[subject] = [grade]

    def get_average_test(self, subject: str = None):
        return self.__average_grade('_testes', subject)

    def get_average_grade(self, subject: str = None):
        return self.__average_grade('_grades', subject)

    def __average_grade(self, dict_name: str, subject):
        dict = getattr(self, dict_name)
        if subject is None:
            ls = []
            for val in dict.values():
                if isinstance(val, list):
                    ls.extend(val)
            return sum(ls) / len(ls) if len(ls) > 0 else None
        else:
            self.__check_subject(subject)
            ls = dict[subject]
            return sum(ls) / len(ls) if len(ls) > 0 else None


stud = Student('Ivan', 'Ivanov')
stud.add_test("algebra", 100)
stud.add_test("algebra", 90)
stud.add_test("biology", 75)
stud.add_test("biology", 85)

stud.add_subject("chemistry")
stud.add_grade('chemistry', 4)
stud.add_grade('chemistry', 5)
print(f'Средний бал {stud} тестов по алгебре = {stud.get_average_test("algebra")}')
print(f'Средний бал {stud} тестов по всем предметам = {stud.get_average_test()}')

print(f'Средняя оценка {stud} по химии = {stud.get_average_grade("chemistry")}')
print(f'Средняя оценка {stud} по всем предметам = {stud.get_average_grade()}')
