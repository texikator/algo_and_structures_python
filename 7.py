"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

fst_length = float(input('Длина отрезка 1 ?: '))
sknd_length = float(input('Длина отрезка 2 ?: '))
thrd_length = float(input('Длина отрезка 3 ?: '))

#проверка длины. Если одна из сторон больше суммы двух других - треугольник возможен
def check_length(a,b,c):
    if (a < b + c) or (b < a + c ) or (c < a + b):
        return True
    else:
        return False

if check_length(fst_length, sknd_length, thrd_length):
    if fst_length == sknd_length == thrd_length:
        print('Треугольник равносторонний')
    if (fst_length == sknd_length and fst_length != thrd_length) or (fst_length == thrd_length and fst_length !=sknd_length) or (sknd_length == thrd_length and sknd_length !=fst_length):
         print('Треугольник равнобедренный')    
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')



