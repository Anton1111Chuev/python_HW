"""Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл."""
import csv
import json
import random
from typing import Callable

CSV_FILE_NAME = 'test_csv.csv'
JSON_FILE_NAME = 'test_json.json'


def decor_run_for_csv_data(func: Callable):
    def wrapper():
        res = []
        with (open(CSV_FILE_NAME, 'r', newline='\n', encoding='utf-8') as f_csv):
            csv_reader = csv.reader(f_csv)
            for i, line in enumerate(csv_reader):
                if i:
                    dict = {
                        'param': str(line),
                        'result': str(func(*[int(iter) for iter in line])),
                    }
                    res.append(dict)
        return res

    return wrapper


def decor_json_save(func: Callable):
    def wrapper(*args, **kwargs):
        with(open(JSON_FILE_NAME, 'w', encoding='utf-8', newline='\n') as f_json):
            json.dump(func(*args, **kwargs), f_json, indent=4)

    return wrapper


@decor_json_save
@decor_run_for_csv_data
def quadratic_equation(a: int | float = 0, b: int | float = 0, c: int | float = 0):
    d = b ** 2 - 4 * a * c
    '''насколько помню из курса математики корня всегда 2 но иногда они совпадают (когда d=0)
       поэтому возвращаем всегда список, возможно ошибаюсь...но суть это особо не  меняет '''
    return [(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]


def init_cvs_file(count_rows_csw: int = 100):
    with (open(CSV_FILE_NAME, 'w', newline='\n', encoding='utf-8') as f_csv):
        writer = csv.DictWriter(f_csv, delimiter=",", fieldnames=['a', 'b', 'c'])
        writer.writeheader()
        writer.writerows({'a': random.randint(1, 200),
                          'b': random.randint(1, 200),
                          'c': random.randint(1, 200)
                          } for _ in range(count_rows_csw))


init_cvs_file()
quadratic_equation()
