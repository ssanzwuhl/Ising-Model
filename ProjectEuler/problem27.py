from itertools import count
from math import sqrt

def is_prime(p):
    if p<=0:
        return False
    for i in range(2, int(sqrt(p))+1):
        if not p%i:
            return False
    return True

def seq(a,b):
    for n in count(0):
        a_n = n**2 + a*n + b
        if not is_prime(a_n):
            return n

values = []
for a in range(-999, 999):
    for b in range(1000):
        values.append((seq(a, b), a*b))

print(max(values)[1])
