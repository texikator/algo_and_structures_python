# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = input('Число 1: ')
b = input('Число 2: ')
c = input('Число 3: ')

if (a == b or a == c or a ==c):
    print('Невозможно найти среднее число')
else:
    if (a < b < c ) or ( a > b > c):
        print(f'Среднее число - {b}')
    elif (b < a < c) or (b > a > c):
        print(f'Среднее число - {a}')
    else:
        print(f'Среднее число - {c}')