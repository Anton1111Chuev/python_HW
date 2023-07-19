"""Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали.
Превратите функции в методы класса.
Задачи должны решаться через вызов методов экземпляра."""

""" Задача:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке.100-1000 строк.
сохранение переданных параметры и результаты работы
функции в json файл."""

import csv
import json
from random import randint

CSV_FILE_NAME = 'test_csv.csv'
JSON_FILE_NAME = 'test_json.json'


class Equation:
    def __init__(self, csv_f_name, json_f_name):
        self.json_f_name = json_f_name
        self.csv_f_name = csv_f_name
        self.data = []

    def init_cvs_file(self, count_rows_csw: int = 100):
        with (open(self.csv_f_name, 'w', newline='\n', encoding='utf-8') as f_csv):
            writer = csv.DictWriter(f_csv, delimiter=",", fieldnames=['a', 'b', 'c'])
            writer.writeheader()
            writer.writerows({'a': randint(1, 200),
                              'b': randint(1, 200),
                              'c': randint(1, 200)
                              } for _ in range(count_rows_csw))

    def _quadratic_equation(self, a: int | float = 0, b: int | float = 0, c: int | float = 0):
        d = b ** 2 - 4 * a * c
        dict = {
            'param': {
                'a': a,
                'b': b,
                'c': c
            },
            'result': [str((-b + d ** 0.5) / (2 * a)), str((-b - d ** 0.5) / (2 * a))],
        }
        self.data.append(dict)

    def add_data_from_csv(self):
        with (open(self.csv_f_name, 'r', newline='\n', encoding='utf-8') as f_csv):
            csv_reader = csv.reader(f_csv)
            for i, line in enumerate(csv_reader):
                if i:
                    self._quadratic_equation(*[int(iter) for iter in line])

    def export_data_json(self):
        with(open(self.json_f_name, 'w', encoding='utf-8', newline='\n') as f_json):
            json.dump(self.data, f_json, indent=4)


eq = Equation(CSV_FILE_NAME, JSON_FILE_NAME)
eq.init_cvs_file()
eq.add_data_from_csv()
eq.export_data_json()
