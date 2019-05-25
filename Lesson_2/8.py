"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

метод с делением имеет недостаток (для меня, не совсем понимаю, что делать в случае, если мы ищем результат для 0, в числе 100.
 В случае с проходом по строке как по массиву этой проблемы не возникнет. и можно не преобразовывать строку в число.

 )


def check_number_str(num, check):

    num = str(num)
    check = str(check)
    result = 0

    for i in range(0, len(num)):
        if num[i] == check:
            result += 1
    return result   



"""


def check_number(number, check, length=1, result=0):

    if number > 0:
        length = len(str(number))
        deci = 10 ** (length - 1)
        digit = number // deci

        if digit == check:
            result += 1
        number %= deci

        return check_number(number, check, length, result)
    else:
        return result
     


result = 0
digit = int(input('Введите цифру: '))
num = int(input('ВВедите количество чисел: '))

for i in range(0, num):
    number = int(input('Введите число: '))
    result += check_number(number, digit)

print(f'Веедено {num} чисел(а). Искомая цифра {digit} встречается в них {result} раз')

