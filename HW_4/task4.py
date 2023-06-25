"""Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список."""

'''
Напишите программу банкомат. 
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''
MULTIPLICITY = 50
PROC_MINUS = 1.5
MAX_PROC_MINUS = 600
MIN_PROC_MINUS = 30
NUMBER_OREPATION_FOR_ADD = 3
PROC_NUMBER_OPERATION = 3
TAX = 10
MAX_SUMM = 5_000_000


def count_tax(sum):
    res = 0
    if sum > MAX_SUMM:
        res = sum * TAX / 100
    return res

def add_procent(sum, count):
    res = 0
    if sum != 0 and count % NUMBER_OREPATION_FOR_ADD == 0:
        res = sum * PROC_NUMBER_OPERATION/100
    return res

def add_money(cur_sum : int, summ : int, count : int):
    return summ + cur_sum + add_procent(summ + cur_sum, count)

def minus_money(cur_sum : int, summ : int, count : int):

    summ_procent = cur_sum * PROC_MINUS/100
    if summ_procent < MIN_PROC_MINUS:
        summ_procent = MIN_PROC_MINUS
    elif summ_procent > MAX_PROC_MINUS:
        summ_procent = MIN_PROC_MINUS

    res = summ - cur_sum - summ_procent
    res = res + add_procent(res, count)

    if res < 0:
        print("Не достаточно денег")
        return summ

    return res

lst_log = []
summ = 0
count = 0

while True:
    dict = {'1': add_money, '2': minus_money}
    num_operation = input("1 - пополнение   2 - снятие   3 - выход ")
    if num_operation == "3":
        break
    elif num_operation == "1" or num_operation == "2":
        count += 1
        dict_log = {"Type": num_operation, "Summ_before": summ, "Count": count}
        summ = summ - count_tax(summ)
        cur_sum = int(input("Введите сумму "))
        if cur_sum % MULTIPLICITY != 0:
            print(f"Сумма должна быть кратна {MULTIPLICITY}")
            continue
        summ = dict[num_operation](cur_sum, summ, count)
        print(f"Общая сумма {summ}")
        dict_log["Summ_after"] = summ
        lst_log.append(dict_log)
    else:
        print("Неправильное значение повторите ввод")

print(lst_log)
