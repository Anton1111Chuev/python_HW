"""Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>"""
import os


def rename_files(finish_name: str, extension_finish: str, extension_start):
    extension_finish = f'.{extension_finish}' if extension_finish[0] != '.' else extension_finish
    extension_start = f'.{extension_start}' if extension_start[0] != '.' else extension_start
    pos = 1
    for obj in os.listdir():
        start_name, extension_current_file = os.path.splitext(obj)
        if extension_current_file == extension_start:
            os.rename(obj, f'{start_name}_{finish_name}_{pos}{extension_finish}')
            pos += 1


rename_files("newname", ".txt", ".txt")
