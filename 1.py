"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter
from collections import deque



s = "hello to all"


def tree(s):

    freq_basic = Counter(s)
    sorted_elements = deque(sorted(freq_basic.items(), key=lambda item: item[1]))
    print(sorted_elements)
    if len(sorted_elements) != 1:
    #print(sorted_elements)
        while len(sorted_elements) > 1:
            freak = sorted_elements[0][1] + sorted_elements[1][1]

            print(freak)

            comb = { 0: sorted_elements.popleft()[0],
                     1: sorted_elements.popleft()[0]
                     }

            for item, _count in enumerate(sorted_elements):
                print(item, _count)
                if freak  > _count[1]:
                    continue

                else:
                    sorted_elements.insert(item, (comb, freak))
                    break
        else:
            sorted_elements.append((comb, freak))

    else:
        frek = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, freak))

    return sorted_elements[0][0]


code_table = dict()

def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')
haffman_code(tree(s))


for i in s:
    print(code_table[i], end=' ')
print()


