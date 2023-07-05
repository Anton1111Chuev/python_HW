"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""


def list_gen(ls_name: list[str], ls_gross: list[int], ls_per: list[str]):
    return {ls_name[i]: ls_gross[i] * float(per[:-1]) / 100 for i, per in enumerate(ls_per) }


print(list_gen(['Иван', 'Илья'], [1000, 900], ['10.25%', '100.5%']))