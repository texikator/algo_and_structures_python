"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import cProfile, timeit, json

number = 345737845309495830672987654345678906856790589534958094313264833294052389457089437593487590347509283457034298750348276585931046813463160315965506304589345143889751093487509314875893147508931470893475984317095874510873487658347083175834058475
number = 13
number = 234
number = 2345
#number = int(input('Введите число'))


def get_deci(num):
    i = 1
    while num // i >= 1:
        i *= 10
    return i/10


def recursion_1(num=number, new_number=''):
    deci = get_deci(num)
    digit = int(num // deci)
    if deci > 1:
        return recursion_1(num % deci, f'{digit}{new_number}')
    if deci == 1:
        return f'{digit}{new_number}'


def recursion_2(num=number, new_number=''):
    deci = 10 ** (len(str(num)) - 1)

    digit = str(num // deci)
    if deci > 1:
        return recursion_2(num % deci, f'{digit}{new_number}')
    else:
        return f'{digit}{new_number}'


def use_list(number=number):
    str_number = str(number)
    result = []
    for i in range(len(str_number)):
        result.insert(0, str_number[i])
    
    return ('').join(result)

def use_list_2(number=number):
    str_number = str(number)
    result = []
    for i in str_number:
        result.insert(0,i)
    return result

def simple(number=number):
    str_num = str(number)
    return str_num[::-1]

def main():

    for i in range(100):
        recursion_1(number)
        recursion_2(number)
        use_list(number)
        simple(number)

cProfile.run('main()')


statistics = []
for i in range(10):

    number = int(f'{str(number)}{str(i)}')
    data = {}
    # print(f"recursion_1: {timeit.timeit('recursion_1()', setup='from __main__ import recursion_1', number=1000)}")
    # print(f"recursion_2: {timeit.timeit('recursion_1', setup='from __main__ import recursion_1', number=10000)}")
    # print(f"use_list: {timeit.timeit('use_list()', setup='from __main__ import use_list', number=10000)}")
    # print(f"use_list_2: {timeit.timeit('use_list_2', setup='from __main__ import use_list_2', number=10000)}")
    # print(f"simple: {timeit.timeit('simple()', setup='from __main__ import simple', number=10000)}")
    data['number'] = number
    data['recursion_1'] = timeit.timeit('recursion_1()', setup='from __main__ import recursion_1', number=1000)
    data['recursion_2'] = timeit.timeit('recursion_2', setup='from __main__ import recursion_2', number=10000)
    data['use_list'] = timeit.timeit('use_list()', setup='from __main__ import use_list', number=10000)
    data['use_list_2'] = timeit.timeit('use_list_2', setup='from __main__ import use_list_2', number=10000)
    data['simple'] = timeit.timeit('simple()', setup='from __main__ import simple', number=10000)

    statistics.append(data)

print(json.dumps(statistics, indent=4))


# Не ожидал что штатный метод [::-1] настолько проигрывает рекурсии в варианте 2
