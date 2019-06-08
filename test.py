import timeit, random, cProfile

length = 100000000

def iter_1(array):
    max = array[0]
    for i in range(length):
        if array[i] > max:
            max = array[i]
            idx = i

    print(max, idx)

def iter_2(array):
    max = array[0]

    for idx, item in enumerate(array):
        if item > max:
            max = item
            index = idx

    print(max, index)

def main():
    array = [random.randrange(-1000, 1000) for i in range(length)]

    iter_1(array)
    iter_2(array)

str = '234234234'

cProfile.run('main()')

# в процессе выполнения утилизировано около 3,5 гигов оперативной памяти.
# ncalls  tottime  percall  cumtime  percall filename: lineno(function)
#         1    1.723    1.723  218.242  218.242 < string > : 1( < module > )
# 100000000   78.910    0.000  158.654    0.000 random.py: 174(randrange)
# 100000000   55.682    0.000   79.744    0.000 random.py: 224(_randbelow)
# 1    8.255    8.255    8.256    8.256 test.py: 14(iter_2)
# 1    0.005    0.005  216.519  216.519 test.py: 24(main)
#         1   35.653   35.653  194.307  194.307 test.py: 25(< listcomp > )
#         1   13.944   13.944   13.952   13.952 test.py: 5(iter_1)
#         1    0.002    0.002  218.244  218.244 {built-in method builtins.exec}
#         2    0.008    0.004    0.008    0.004 {built-in method builtins.print}
# 100000000    7.676    0.000    7.676    0.000 {method 'bit_length' of 'int' objects}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 102398007   16.386    0.000   16.386    0.000 {method 'getrandbits' of '_random.Random' objects}
