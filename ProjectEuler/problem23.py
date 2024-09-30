from time import time
def can_be_written(n):
    for i in abundants_list:
        if i>n:
            return False
        if n-i in abundants_set:
            return True
t0 = time()
top = 28123 
sum_list = [0]*top
for i in range(1, top//2+1):
    for j in range(2*i, top, i):
        sum_list[j]+=i #Using factors' property.
abundants_list = [x for x in range(top) if x<sum_list[x]]
abundants_set = set(abundants_list)
print("The answer is", sum([x for x in range(top) if not can_be_written(x)]), "and it took me", time()-t0, "s")