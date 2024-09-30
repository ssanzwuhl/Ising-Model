from functools import reduce
from math import sqrt
def num_factors(n):    
    return len(set(k for i in range(1, int(sqrt(n))+1) if not n%i for k in (i, n//i)))
iterator=1
i=1
top=500
while num_factors(iterator)<top:
    i+=1
    iterator+=i
    #print(iterator)
print(iterator)
