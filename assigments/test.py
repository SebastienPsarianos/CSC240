from math import floor, ceil
from random import randint

def sort_by_thirds(L, i, j):
    t = 0
    t =+ 1
    if j-i >= 2:
        m = floor((j-i+1)/3)
        t =+ sort_by_thirds(L, i, j - m)
        t =+ sort_by_thirds(L, i + m, j)
        t =+ sort_by_thirds(L, i, j - m)
    t += 1
    if j-i == 1:
        t += 1
        if L[j] < L[i]:
            x = L[j]
            L[j] = L[i]
            L[i] = x
    return t

def t(n):
    if n < 2:
        return 3
    else:
        return 3 * t(ceil(2*n/3 - 1/3)) + 1

lst = []
for i in range(200):
    lst.append(randint(1, 10000))
res = []
for i in range(2, 100):
    res.append((i-1, sort_by_thirds(lst, 1, i)))
theory = []
for i in range(2, 200):
    theory.append((i - 1, t(i-1)))

print(theory)

print(res)



