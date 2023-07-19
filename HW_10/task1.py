"""Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""


class Animal:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} - {self.get_into_about_unique_param()}'

    def get_into_about_unique_param(self):
        return ""


class Bird(Animal):
    def __init__(self, name: str, wings: int):
        super().__init__(name)
        self.wings = wings

    def get_into_about_unique_param(self):
        res = ""
        if self.wings <= 10:
            res = "маленький размах крыльев"
        elif 10 < self.wings < 20:
            res = "средний размах крыльев"
        else:
            res = "большой размах крыльев"
        return res


class Mammals(Animal):

    def __init__(self, name: str, wool: int):
        super().__init__(name)
        self.wool = wool

    def get_into_about_unique_param(self):
        res = ""
        if self.wool <= 10:
            res = "короткошерстная"
        else:
            res = "длинношерстная"
        return res


class Fish(Animal):

    def __init__(self, name: str, depth: int):
        super().__init__(name)
        self.depth = depth

    def get_into_about_unique_param(self):
        res = ""
        if self.depth <= 10:
            res = "живет на небольшой глубине"
        elif 10 < self.depth < 100:
            res = "живет на средней глубине"
        else:
            res = "глубоководная рыба"
        return res


class Fabric:
    @staticmethod
    def create_object(class_name: str, *args, **kwargs):
        class_name = class_name.capitalize()
        class_name_dict = {
            "Animal": Animal,
            "Bird": Bird,
            "Mammals": Mammals,
            "Fish": Fish,
        }

        class_obj = class_name_dict.get(class_name)
        if class_obj:
            return class_obj(*args, **kwargs)


lynx = Fabric.create_object("Mammals", "Рысь", 20)
print(lynx)

hyena = Fabric.create_object("Mammals", "Гиена", 3)
print(hyena)

shark = Fabric.create_object("Fish", "Акула", 15)
print(shark)

eagle = Fabric.create_object("Bird", "Орел", 20)
print(eagle)
