# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = float(input('Введите координату X первой точки: '))
y1 = float(input('Введите координату Y второй точки: '))
x2 = float(input('Введите координату X второй точки: '))
y2 = float(input('Введите координату Y второй точки: '))

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

print(f'уравнение прямой: y = {k}x + {b}')