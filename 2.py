"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

#s = input('Введите строку из строчных латинских букв: ')

s = "hello to all peoples"




def without_sha(s):
    n = len(s)
    cnt = set()
    for i in range(n):

            
        for j in range(i+1, n+1):

            if i == 0 and j == n:
                continue
            substr = s[i:j]
            #print(i, j, substr)
            cnt.add(substr)
            #j += 1
    return cnt

result = without_sha(s)


def with_sha(s):
    n = len(s)
    cnt = set()
    for i in range(n):
        for j in range(i+1, n+1):

            if i == 0 and j == n:
                continue
            
            h_substr = hashlib.sha1(s[i:j].encode('utf8')).hexdigest()
            cnt.add(h_substr)
    
    return cnt

result_sha = with_sha(s)
print(f'Количество элементов: {len(result)}, уникальные подстроки {result}')
print(f'Количество элементов: {len(result_sha)}, уникальные подстроки (sha1) {result_sha}')
