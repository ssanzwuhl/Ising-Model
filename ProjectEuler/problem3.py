from time import time
def prime_fac(n):
    x=2
    while n>1:
        if not n%x:
           n//=x
        else:
            x+=1
    return x
t0=time()
print(prime_fac(600851475143), time()-t0)

