"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку."""
import csv
import pickle

f_list =[]
with (open('test_list_dict.csv', 'r', newline='\n', encoding='utf-8') as f_csv,):
    for i, f_data in enumerate(csv.reader(f_csv)):
        f_list.append(f_data)
res_pikle = pickle.dumps(f_list, protocol=pickle.DEFAULT_PROTOCOL)
print(res_pikle)