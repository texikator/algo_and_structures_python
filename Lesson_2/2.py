"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

def get_deci(num):
    i = 1
    while num // i >= 1:
        i *= 10
    return i/10


def calc(num, count_chet, count_nchet):

    deci = get_deci(num)

    i = num // deci

    if i % 2 == 0:
        count_chet += 1
        print(f'цифра {i} - четная')
    else:
        count_nchet += 1
        print(f'Цифра {i} - нечетная' )
    if deci > 1:
        return calc(num % deci, count_chet, count_nchet)
    elif deci == 1:
        return "Четные: " + str(count_chet)+" Нечетные:"+str(count_nchet)


print(calc(int(input('Введите число')),0,0))
