"""Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""
import os


def file_parts(file_path: str):
    path, file_name = os.path.split(file_path)
    name, extension = os.path.splitext(file_name)
    return path, name, extension

def file_parts_without_os(file_patch: str):
    *path, file_name = file_patch.split('/')
    name, extension = file_name.split('.')
    return '/'.join(path), name, f'.{extension}'

print(file_parts('C:/Users/user1/Desktop/Лекции/Коллекции.pdf'))
print(file_parts_without_os('C:/Users/user1/Desktop/Лекции/Коллекции.pdf'))