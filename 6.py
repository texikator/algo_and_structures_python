# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы: '))

a_pos = ord('a')
alph_length = 26

if num > 0 and num < 27:
    print(f'Это буква: {chr(a_pos + num -1)}')
else:
    print('Номер не соответсвует букве алфавита')
