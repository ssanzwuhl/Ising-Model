from time import time
from itertools import count
def sixn():
    yield 2
    yield 3
    for i in count(6,6):
        yield i-1
        yield i+1
def primes_until(m):
    sieve=[True]*m
    for i in sixn():
        if i>m:
            break
        if sieve[i]:
            yield i
            for mult in range(i*i, m, i):
                sieve[mult]=False
t0=time()
top=2 * 10 ** 6
print(sum(primes_until(top)), time()-t0)