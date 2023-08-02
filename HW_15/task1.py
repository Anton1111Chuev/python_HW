'''
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

import argparse
import os
from collections import namedtuple
import logging


def get_info_about_file(directory_path=''):
    if directory_path == '':
        directory_path = os.getcwd()
    entries = os.scandir(directory_path)
    Item = namedtuple('Item', ['name', 'extension', 'is_directory', 'parent_directory'])
    items = []
    for entry in entries:
        name = os.path.splitext(entry.name)[0]
        extension = os.path.splitext(entry.name)[1] if not entry.is_dir() else ""
        is_directory = entry.is_dir()
        parent_directory = os.path.basename(os.path.normpath(directory_path))
        items.append(Item(name, extension, is_directory, parent_directory))

    logging.basicConfig(filename='test.log.', filemode='a',
                        encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger('Get info about file:')
    logger.info(f'in:{directory_path}, out:{items}')

    return items


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-directory_path', metavar='directory_path', type=str, default='')
    args = parser.parse_args()
    res = get_info_about_file(args.directory_path)
    print(res)
