"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import math, timeit, sys
from memory_profiler import profile
from pympler import asizeof
sys.setrecursionlimit(100000)
#без решета, рекурсия

@profile
def get_simple_recursion(num_count, finded=[], number=3):

    for i in range(2, int(math.sqrt(number))+1):

        print(i)
        if number % i == 0:
            break
    else:
         finded.append(number)
         #print(number, end=" ")
         #print(finded)
         #print("sdfsdf", len(finded))
         
    number += 2
    
    if len(finded) == num_count:
        return finded
    else:
        return get_simple_recursion(num_count, finded, number)



#без решета, без рекурсии
@profile
def get_simple(num_count=15000, number=2):
    finded = []
    print(f'размер массива простых чисел в начале {asizeof.asizeof(finded)}')
    simple_count = 0
    while simple_count < num_count:
        
        div = 2
        
        while 2 <= div <= int(math.sqrt(number))+1:

            if number % div == 0 and number != div:
                break
            div += 1
            
        else:
            finded.append(number)
            simple_count += 1
            print(len(finded))
        number += 1
    print(f'размер массива простых чисел в конце {asizeof.asizeof(finded)}')
    return finded



#num_count = int(input('Введите номер числа: '))
#num_count  = 500
#simple_numbers = get_simple(num_count)

#print(f' Метод 1: заданное число: {simple_numbers[-1]} ')
#print(f'Метод 1: Список простых чисел: {simple_numbers}')

#n = int(input('Введите границу вычисление'))


@profile
def eratos(n=163841):
    finded = []
    a = [i for i in range(1, n+1)]
    a[0] = 0

    number = 1
    step = 1
    while number < n:
        
        if a[number] != 0:
            finded.append(a[number])    
            step = a[number]

            for div in range(a[number] ** 2, n+1, step):
                a[div-1] = 0
            
        number += 1
        
#    for i in a:
#        if a > 0:
#            finded.append(a)
    return finded

#print(print(f'Метод 2: Список простых чисел: {eratos(n)}'))
#print(get_simple(800))


def function():
    c = get_simple(15000)
    print(c[-1])
    #get_simple_recursion(500)
    eratos(c[-1])
    print(timeit.timeit('get_simple()', setup='from __main__ import get_simple'))
    print(timeit.timeit('eratos()', setup='from __main__ import eratos'))


if __name__ == "__main__":
    function()


# Найдено 15000 простых чисел до 163841
# простой метод оказался более щадящим с точки зрения памяти
#
#
# много памяти ушло на заполнение массива
#
#размер массива найденных простых чисел:
# в начале - 64
# в конце -  604920
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35     15.2 MiB     15.2 MiB   @profile
#     36                             def get_simple(num_count=15000, number=2):
#     37     15.2 MiB      0.0 MiB       finded = []
#     38     15.2 MiB      0.0 MiB       simple_count = 0
#     39     15.8 MiB      0.1 MiB       while simple_count < num_count:
#     40
#     41     15.8 MiB      0.0 MiB           div = 2
#     42
#     43     15.8 MiB      0.0 MiB           while 2 <= div <= int(math.sqrt(number))+1:
#     44
#     45     15.8 MiB      0.0 MiB               if number % div == 0 and number != div:
#     46     15.8 MiB      0.0 MiB                   break
#     47     15.8 MiB      0.0 MiB               div += 1
#     48
#     49                                     else:
#     50     15.8 MiB      0.1 MiB               finded.append(number)
#     51     15.8 MiB      0.0 MiB               simple_count += 1
#     52
#     53     15.8 MiB      0.0 MiB           number += 1
#     54     15.8 MiB      0.0 MiB       return finded
#
#
# 163841
# Filename: C:/Users/u2/Downloads/algo_and_structures_python-master/algo_and_structures_python-master/Lesson_6/eratosfen.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     68     15.9 MiB     15.9 MiB   @profile
#     69                             def eratos(n=163841):
#     70     15.9 MiB      0.0 MiB       finded = []
#     71     23.7 MiB      0.8 MiB       a = [i for i in range(1, n+1)]
#     72     23.7 MiB      0.0 MiB       a[0] = 0
#     73
#     74     23.7 MiB      0.0 MiB       number = 1
#     75     23.7 MiB      0.0 MiB       step = 1
#     76     23.7 MiB      0.0 MiB       while number < n:
#     77
#     78     23.7 MiB      0.0 MiB           if a[number] != 0:
#     79     23.7 MiB      0.0 MiB               finded.append(a[number])
#     80     23.7 MiB      0.0 MiB               step = a[number]
#     81
#     82     23.7 MiB      0.0 MiB               for div in range(a[number] ** 2, n+1, step):
#     83     23.7 MiB      0.0 MiB                   a[div-1] = 0
#     84
#     85     23.7 MiB      0.0 MiB           number += 1
#     86
#     87                             #    for i in a:
#     88                             #        if a > 0:
#     89                             #            finded.append(a)
#     90     23.7 MiB      0.0 MiB       return finded
