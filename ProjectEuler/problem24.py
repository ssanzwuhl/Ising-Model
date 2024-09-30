from itertools import permutations
digits = "0123456789"
dig_per = permutations(digits)
cont = 0
top = 10 ** 6
for i in dig_per:
    cont+=1
    if cont>=top:
        print("".join(i))
        break