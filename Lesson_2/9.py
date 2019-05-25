"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def calc(number, length=1, summ=0):

    if number > 0:
        length = len(str(number))
        deci = 10 ** (length - 1)
        digit = number // deci
        summ += digit
        number %= deci
        
        return calc(number, length, summ)
    else:
        return summ


numbers = input('Введите числа, разделенные запятой: ')

max_summ = 0

for i in numbers.split(','):
    summ = calc(int(i))

    if summ > max_summ:
        max = i
        max_summ = summ

print(f'Максимальная сумма: {max_summ}, число: {max}')

