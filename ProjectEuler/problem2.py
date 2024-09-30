from time import time
def even_fib_til(n):
    a, b = 0, 1
    result=0
    while a<n:
        a, b = b, b+a
        if not a&1:
            result+=a
    return result
t0=time()
print(even_fib_til(4*10**6), time()-t0)
