# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input('Введите трехзначное число: '))

if num > 99 and num < 1000 :
    hundreds = num // 100
    tmp = num % 100
    tens = tmp // 10
    ordinary = tmp % 10
    print(f'сумма составляющих числа {num} цифр: {hundreds + tens + ordinary}, \
              произведение: {hundreds * tens * ordinary}')

else:
    print('Некорректное число')
