"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def left_part(n, iteration=0, summ=0):

    iteration += 1
    summ += iteration

    #print(iteration, summ)
    if iteration == n:
        return summ
    else:
        return left_part(n, iteration, summ)


n = int(input('Введите значение n'))
left = left_part(n)
right = n*(n+1)/2


if left == right:
    print('Равенство верно')
else:
    print('Равенство неверно')

print(f'Значение левой части равно {left}')
print(f'Значение правой части равно {right} ')
