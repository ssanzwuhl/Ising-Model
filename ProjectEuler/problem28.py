top = 1001
counter = 1
for n in range(3, top+1, 2):
    counter += 4 * n ** 2 - 6 * (n - 1) 
print(counter)