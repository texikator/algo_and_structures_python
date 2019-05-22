"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def get_deci(num):
    i = 1
    while num // i >= 1:
        i *= 10
    return i/10


def recursion(num, new_number):
    deci = get_deci(num)
    digit = int(num // deci)
    if deci > 1:
        return recursion(num % deci, str(digit)+str(new_number))
    if deci == 1:
        return str(digit)+str(new_number)


num = int(input('Введите число'))

print(recursion(num, ''))
