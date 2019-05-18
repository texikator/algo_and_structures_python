#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

first_char = input('Первая буква: ').lower()
second_char = input('Вторая буква: ').lower()

a_pos = ord('a')

first_pos = ord(first_char) - a_pos + 1
second_pos = ord(second_char) - a_pos + 1
print(f'Позиция первой буквы: {first_pos}')
print(f'Позиция второй буквы: {second_pos}')
print(f'Расстояние между буквами: {abs(first_pos - second_pos)} ')
