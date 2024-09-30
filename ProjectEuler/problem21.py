from math import sqrt
from time import time
def factor_sum(n):
    return sum([k for i in range(1, int(sqrt(n))+1) if not n%i for k in (i, n//i)])-n
def is_amicable(n):
    a = factor_sum(n)
    return n==factor_sum(a) and a != n
t0 = time()
print(sum([i for i in range(int(1e4)) if is_amicable(i)]), time()-t0)
