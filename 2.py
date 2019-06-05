"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque
from collections import Counter

number_one = input('Введите число 1')
number_two = input('Введите число 2')

one = deque(number_one)
two = deque(number_two)
#print(number_one)


def hex_digit_add(one, two, tmp='0',  result=deque(), position=-2):

    if position == -2:
        if len(one) > len(two):
            position = len(one)
        else:
            position = len(two)

    if position == 0 and tmp == '1':
        sum = hex(int(tmp, 16))
    else:
        sum = hex(int(one.pop(), 16) + int(two.pop(), 16) + int(tmp, 16))

    if len(str(sum)[2:]) > 1:
        result.appendleft(str(sum)[-1])
        tmp = '1'
    else:
        result.appendleft(str(sum)[-1])
        tmp = '0'

    position -= 1

    if position <= 0 and tmp == '0':
        return result
    else:
        return hex_digit_add(one, two, tmp,  result, position)


print(hex_digit_add(one, two))





# def hex_summ(array, tmp='', result=[], position=-1):
#     internal = []
#     if position < 0:
#         for item in array:
#             if len(item) > position:
#                 position = len(item)
#     internal = [[0 for i in range(position)] for i in range(len(array))]

#     for j in range(len(array)):
#         for i in range(position):
#             #print(i, len(array[i]))
#             if i >= position - len(array[j]):
#                 #print(j,i,  i-len(array[j]), array[j][i-len(array[j])])
#                 internal[j][i] = array[j][i-len(array[j])+1]
#             print(i, j)

#     for i in reversed(range(position)):
#         summ = 0x0
#         for j in range(len(array)):
#             #print(internal[j][i], end =" ")
#             summ += hex(int(internal[j][i], 16))
#             print(summ, tmp)
#             #if len(hex(int(summ,16))[2:]) == 2:
#             #    tmp = summ[1:-1]
#         print(summ)    

#     return internal           
#

#print(hex_summ([['b','a'],['b','f','a']]))

