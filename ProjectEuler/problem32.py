from itertools import permutations

perm = permutations(range(1,10))
perm = [''.join(map(str, p) )for p in perm]

#Empezamos con fuerza bruta. La idea es tener 2 cursores: el primero 
#separa el número entre factorfactor producto, y el segundo 
#separa factorfactor en factor factor. 
products = set()
def calc_prod(permutation): #inputs a permutation, as string
    global products
    cursor1 = 5 #La única posibilidad de que exista 'el producto'
                #dentro de la permutación, es que sea de 5 dígitos
    factors = permutation[:cursor1]
    product = permutation[cursor1:]
    for cursor2 in range(2, cursor1):
        factors1 = int(factors[:cursor2])
        factors2 = int(factors[cursor2:])
        if int(product) == factors1 * factors2:
            products.add(int(product))


pi = list(map(calc_prod, perm))

print(sum(products))
