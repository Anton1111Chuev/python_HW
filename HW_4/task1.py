"""Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s)на None.
 Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""

def replace():
    tmp = {}
    for name, val in globals().items():
        if name.endswith('s') and len(name) > 1:
            tmp[name[:-1]], globals()[name] = val, None

    globals().update(tmp)

names = ['Name1', 'Name2']
countes = 27
for_example_s = 2
print(names, countes, for_example_s)
replace()
print(names, countes, for_example_s)
print(name, counte, for_example_)