"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий"""
import csv
import json
import os
import pickle
from pathlib import Path


def info_about_files_recurs(dir_path: str):
    '''обходит рекурсивно все поддиректории и возвращает картеж из списка и общего размера'''
    res = []
    summ_size = 0
    p = Path(dir_path)
    for f in p.iterdir():
        dict = {
            "name": f.name,
            "parent": dir_path,
            "is_file": os.path.isfile(f),
            "size": os.path.getsize(f),
        }
        if os.path.isdir(f):
            cur_ls, cur_size = info_about_files_recurs(os.path.join(dir_path, f.name))
            res.extend(cur_ls)
            dict["size"] += cur_size #размер папки тоже сохраняем
        summ_size += dict["size"]
        res.append(dict)

    return res, summ_size

f_info = info_about_files_recurs("C:/Users/asyac/PycharmProjects/pythonHomeworks/test1")

f_info, *_ = info_about_files_recurs("C:/Users/asyac/PycharmProjects/pythonHomeworks/test1")
print(f_info)
if isinstance(f_info, list) and len(f_info):
    with(
        open('test_json.json', 'w', encoding='utf-8') as f_json,
        open('test_csv.csv', 'w', newline='\n', encoding='utf-8') as f_csv,
        open('test_pickle.pickle', 'wb') as f_pickle,
    ):
        json.dump(f_info, f_json, indent=4)

        pickle.dump(f_info, f_pickle)

        writer = csv.DictWriter(f_csv, delimiter=",", fieldnames=f_info[0].keys())
        writer.writeheader()
        writer.writerows(iter for iter in f_info)