from time import time
t0=time()
print(abs(sum([i**2 for i in range(101)])-sum([i for i in range(101)])**2), time()-t0)