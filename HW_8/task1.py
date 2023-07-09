"""Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестированию возьмите pickle версию файла из предыдущей задачи.
 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла."""
import csv
import pickle


def picle_to_csv(name_pikle, name_csv):
    with (
        open(name_pikle, 'rb') as f_pikle,
        open(name_csv, 'w', newline='\n', encoding='utf-8') as f_csv,
    ):
        new_ls = pickle.load(f_pikle)
        if isinstance(new_ls, list) and len(new_ls):
            writer = csv.DictWriter(f_csv, delimiter=",", fieldnames=new_ls[0].keys())
            writer.writeheader()
            writer.writerows(iter for iter in new_ls)

picle_to_csv('test_list_dict.pickle', 'test_list_dict.csv')