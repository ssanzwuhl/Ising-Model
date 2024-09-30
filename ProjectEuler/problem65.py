from math import ceil
def nthconvergent(n):
    convergents = [1] * n
    for i in range(1, n, 3):
        convergents[i] = ceil(i/3) * 2
    return convergents

print(nthconvergent(11))
