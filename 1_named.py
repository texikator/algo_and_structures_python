import collections

data = collections.namedtuple('Company', 'name first second third fourth')

cnt = int(input('Companies count: '))

profits = []

summ = 0

for item in range(cnt):
    company = input('Company: ')
    quarter = []

    for i in range(4):
        profit = float(input(f'Profit for {i+1} quarter: '))
        quarter.append(profit)
        summ += profit
    profits.append(data(
        name=company,
        first=quarter[0],
        second=quarter[1],
        third=quarter[2],
        fourth=quarter[3]
    ))


def find_average(data):
    summ = 0
    cnt = len(data)
    for i in data:
        summ += i.first + i.second + i.third + i.fourth
    return summ / cnt

def calculate(profits, avg):
    greater = []
    smaller = []
    for i in profits:
        profit = i.first + i.second + i.third + i.fourth
        if profit < avg:
            smaller.append(f'{i.name} - profit {profit}')
        else:
            greater.append(f'{i.name} - profit {profit}')
    print(f'Average: {avg:.3f}')
    print(f' profit greater than average: {", ".join(greater)}')
    print(f' profit smaller than average: {", ".join(smaller)}')


avg = find_average(profits)

calculate(profits, avg)
