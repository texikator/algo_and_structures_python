"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import math, timeit, sys

sys.setrecursionlimit(100000)
# #без решета, рекурсия
# def find_simple(num_count=10, finded=[], number=3):
#     #print('N ',number)
#     for i in range(2, int(math.sqrt(number))+1):
#         #print('i ', i)
#         if number % i == 0:
#             break
#     else:
#          finded.append(number)
#          print(number, end=" ")
#          #print(finded)
#          #print("sdfsdf", len(finded))
#     number += 2         

#     if len(finded) == num_count:
#         return finded
#     else:
#         return find_simple(num_count, finded, number)



#без решета, без рекурсии
def get_simple(num_count=100, number=2):
    finded = []
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
     
        number += 1
    return finded



#num_count = int(input('Введите номер числа: '))
num_count  = 500
simple_numbers = get_simple(num_count)

print(f' Метод 1: заданное число: {simple_numbers[-1]} ')
print(f'Метод 1: Список простых чисел: {simple_numbers}')


n = int(input('Введите границу вычисление'))

def eratos(n=800):
    finded = []
    a = [i for i in range(1,n+1)]
    a[0] = 0

    number = 1
    step =1 
    while number < n:
        
        if a[number] !=0:
            finded.append(a[number])    
            step = a[number]
            #print(f'число в списке {a[number]} ,шаг {step}')
            for div in range(a[number] ** 2, n+1, step):
                a[div-1] = 0
            
        number += 1
        
#    for i in a:
#        if a > 0:
#            finded.append(a)
    return finded

print(print(f'Метод 2: Список простых чисел: {eratos(n)}'))


print(timeit.timeit('get_simple()', setup='from __main__ import get_simple', number=100))
print(timeit.timeit('eratos()', setup='from __main__ import eratos', number=100))

# 0.17245420000000067
# 0.04399160000000002
