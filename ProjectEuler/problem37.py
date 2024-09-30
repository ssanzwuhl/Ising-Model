from itertools import count
#Lo suyo primero sería tener una lista de primos
#Dentro de la lista de primos, quedarse solo con los que son truncables
#Luego para saber si un primo es truncable, hay que saber si una vez se divide entre 10 (truncando a la izquierda) o se le quita el primer número (truncando a la derecha) habría que mirar si está en dicha lista, por que tiene que haber aparecido antes.


#Forma naive de saber si un número es primo
def is_prime(p): #Mi forma de ver si un número es primo
    for i in range(3, int(p**.5) +1, 2):
        if not p%i:
            return False
    return True
#Generador de primos, a ver si me acuerdo

def sixn():
    yield 2
    yield 3
    for n in count(1):
        yield 6 * n + 1
        yield 6 * n - 1

def sieve(n):
    primes = [True] * n #Asumo que todos los números son primos
    for i in sixn(): #Todos los posibles números primos son de la forma 6n +/- 1
        if i>n:
            break
        if primes[i]: #
            for x in range(i**2, n, i):
                primes[x] = False               
            yield i

print(list(sieve(198)))

def is_truncatable(p):
    
