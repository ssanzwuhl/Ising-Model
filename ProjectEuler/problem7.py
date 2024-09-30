from math import sqrt
from itertools import count
def is_prime(n):
    if not n&1:
        return False
    if n<=3:
        return True
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0:
            return False
    return True
top=10001
prime=0
for i in count(0,6):
    if is_prime(i-1):
        prime+=1
        if prime>=top:
            print(i-1)
            break
    if is_prime(i+1):
        prime+=1
        if prime>=top:
            print(i+1)
            break





