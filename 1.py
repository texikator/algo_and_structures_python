# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

orders = [int(i) for i in range(2, 10)]
numbers = [int(i) for i in range(2, 100)]

multi = [0 for i in range(2,10)]


for order in orders:
    print(order)
    for number in numbers:
        #print(number, order)
        if number % order == 0:
            #print(order)
            multi[order-2] += 1
#print(multi)

output = f'Числа в интервале 2..9 и количества кратных им чисел: '
for i in multi:
    print(i)
    output += f'{i+2}-{i}, '
    
print(output)

