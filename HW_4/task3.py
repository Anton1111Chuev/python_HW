"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
 где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление."""

def kwd_transporate(**kwargs):
    res = {}
    for k, v in kwargs.items():
        if ''.join(dir(v)).find('__hash__') and v.__hash__ != None:
            res[v] = k
        else:
            res[str(v)] = k
    return res

print(kwd_transporate(lst=[1, 2], num=1, st='test'))
