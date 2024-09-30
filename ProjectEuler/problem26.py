def ld(p, q):
    while p<q:
        p *= 10
    p_ = p%q 
    cont = 0
    quotients = set()
    while p_ not in quotients:
        quotients.add(p_)
        p_ = p_%q * 10
        cont += 1
    return cont

print(max([ld(1, i) for i in range(1, 1000)]))