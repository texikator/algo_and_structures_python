import collections


cnt = int(input('Введите количество предприятий: '))


profits = []
summ = 0
for profit in range(cnt):

    company = input('Введите название компании: ')
    for i in range(4):

        profit = float(input(f'Прибыль за {i+1} квартал:'))
        prof = (company, profit)
        profits.append(prof)
        summ += profit


data = collections.defaultdict(float)

for k, v in profits:
    data[k] += v

avg = summ / cnt

print(f'средняя прибыль: {avg:.3f}')
greater = []
smaller = []
for k, v in data.items():
    if v < avg:
        smaller.append(f'{k} -  прибыль {v}')
    else:
        greater.append(f'{k} -  прибыль {v}')

print(f' Предпириятия с большей прибылью: {", ".join(greater)}')
print(f' Предпириятия с меньшей прибылью: {", ".join(smaller)}')