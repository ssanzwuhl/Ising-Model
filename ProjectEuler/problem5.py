from itertools import count

def lcm(values):
    n = max(values)
    for i in count(1):
        if not (n * i)%min(values):
            return n * i
    
value = 1
i = 20
a = (2, 1)
for j in range(1, 20):
    a = (j, lcm(a))
print(lcm(a))