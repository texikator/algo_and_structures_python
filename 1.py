"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from memory_profiler import profile
from pympler import asizeof

# перевернуть число
#все методы при данном исходном значении уместились в 16 MiB
#изменения в объеме памяти приходились на добавление элементов к результирующей строке/массиву

number = 345737845309495830672987654345678906856790589534958094313264833294052389457089437593487590347509283457034298750


def get_deci(num):
    i = 1
    while num // i >= 1:
        i *= 10
    return i / 10


@profile
def recursion_1(num=number, new_number=''):
    deci = get_deci(num)
    digit = int(num // deci)
    if deci > 1:
        return recursion_1(num % deci, f'{digit}{new_number}')
    if deci == 1:
        return f'{digit}{new_number}'


@profile
def recursion_2(num=number, new_number=''):
    deci = 10 ** (len(str(num)) - 1)

    digit = str(num // deci)
    if deci > 1:
        return recursion_2(num % deci, f'{digit}{new_number}')
    else:
        
        return f'{digit}{new_number}'


@profile()
def use_list(number=number):
    str_number = str(number)
    result = []
    for i in range(len(str_number)):
        result.insert(0, str_number[i])

    return ('').join(result)


@profile
def use_list_2(number=number):
    str_number = str(number)
    result = []
    for i in str_number:
        result.insert(0, i)
    return result


@profile
def simple(number=number):
    str_num = str(number)
    return str_num[::-1]


@profile
def function():
    print(recursion_1(number))
    print(recursion_2(number))
    print(use_list(number))
    print(simple(number))
    print("q")


if __name__ == "__main__":
    #print("q")
    function()



# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30                                     return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.1 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     16.0 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.9 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.8 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.8 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.8 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.8 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.8 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.8 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.8 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.8 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.1 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.7 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.6 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.5 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     16.1 MiB     15.4 MiB   @profile
#     26                             def recursion_1(num=number, new_number=''):
#     27     16.1 MiB      0.0 MiB       deci = get_deci(num)
#     28     16.1 MiB      0.0 MiB       digit = int(num // deci)
#     29     16.1 MiB      0.0 MiB       if deci > 1:
#     30     16.2 MiB      0.0 MiB           return recursion_1(num % deci, f'{digit}{new_number}')
#     31     16.1 MiB      0.0 MiB       if deci == 1:
#     32     16.1 MiB      0.0 MiB           return f'{digit}{new_number}'


# 84655332923193239167915429234528692552671824786797138631597536146385635356862675492859493548737543
# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41                                     return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.2 MiB      0.0 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     16.2 MiB     16.2 MiB   @profile
#     36                             def recursion_2(num=number, new_number=''):
#     37     16.2 MiB      0.0 MiB       deci = 10 ** (len(str(num)) - 1)
#     38
#     39     16.2 MiB      0.0 MiB       digit = str(num // deci)
#     40     16.2 MiB      0.0 MiB       if deci > 1:
#     41     16.3 MiB      0.1 MiB           return recursion_2(num % deci, f'{digit}{new_number}')
#     42                                 else:
#     43     16.2 MiB      0.0 MiB           return f'{digit}{new_number}'


# 05789243754382957439578439573498754983254923384623134985943598597658698765434567892763859493548737543
# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     46     16.3 MiB     16.3 MiB   @profile()
#     47                             def use_list(number=number):
#     48     16.3 MiB      0.0 MiB       str_number = str(number)
#     49     16.3 MiB      0.0 MiB       result = []
#     50     16.3 MiB      0.0 MiB       for i in range(len(str_number)):
#     51     16.3 MiB      0.0 MiB           result.insert(0, str_number[i])
#     52
#     53     16.3 MiB      0.0 MiB       return ('').join(result)


# 057892430754382905743095784395734980754983250492338462313490859435985097658609876543456789276038594903548737543
# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     65     16.3 MiB     16.3 MiB   @profile
#     66                             def simple(number=number):
#     67     16.3 MiB      0.0 MiB       str_num = str(number)
#     68     16.3 MiB      0.0 MiB       return str_num[::-1]


# 057892430754382905743095784395734980754983250492338462313490859435985097658609876543456789276038594903548737543
# q
# Filename: 1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     71     15.4 MiB     15.4 MiB   @profile
#     72                             def function():
#     73     16.2 MiB      0.8 MiB       print(recursion_1(number))
#     74     16.3 MiB      0.1 MiB       print(recursion_2(number))
#     75     16.3 MiB      0.0 MiB       print(use_list(number))
#     76     16.3 MiB      0.0 MiB       print(simple(number))
#     77     16.3 MiB      0.0 MiB       print("q")


