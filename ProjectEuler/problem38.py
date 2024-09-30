from itertools import count
from time import time 

#Primero quiero hacer una función que genere el producto de n con (1, 2, 3, ...) y si se repiten 2 números o el resultado es un número de longitud mayor a 9 dígitos, se cancela.

def pandigital_product(N):
    result = "" 
    for i in count(1):
        Ni = str(N * i)
        if '0' in Ni:
            return False
        result += str(N*i)

        if len(result)!=len(set(result)) or len(result)>9:
            return False

        if len(result)==9:
            return result

#Como el mayor va a empezar por 9, entonces quiero que todos empiecen por 9. 

t0 = time()

results = []

candidates = [num for num in range(1, 100000, 2) if num%5!=0] 

for i in candidates[::-1]:
    i = int('9' + str(i))

    a = pandigital_product(i)
    if a != False:
        results.append(a)

print(max(results), time() - t0)

