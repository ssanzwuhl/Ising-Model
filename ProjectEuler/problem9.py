from math import sqrt
from time import time
class Breaker(Exception):
    pass
p=1000
t0=time()
try:
    for m in range(1, p):
        for n in range(1, m):
            if 2 * m ** 2 + 2 * m * n  == p:
                print(2*m**5*n - 2*m*n**5)
                raise Breaker
except Breaker:
    pass
