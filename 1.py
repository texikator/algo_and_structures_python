"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

cnt = int(input('Введите количество предприятий: '))


profits = {}
summ = 0
for i in range(cnt):
    company_profit = 0
    company = input('Название компании: ')
    for i in range(4):
        profit = float(input(f'Прибыль за {i+1} квартал: '))
        company_profit += profit
        summ += profit
    profits[company] = company_profit

avg = summ / cnt

print(f'средняя прибыль: {avg:.3f}')
greater = []
smaller = []
for k, v in profits.items():
    if v < avg:
        smaller.append(f'{k} -  прибыль {v}')
    else:
        greater.append(f'{k} -  прибыль {v}')

print(f' Предпириятия с большей прибылью: {", ".join(greater)}')
print(f' Предпириятия с меньшей прибылью: {", ".join(smaller)}')