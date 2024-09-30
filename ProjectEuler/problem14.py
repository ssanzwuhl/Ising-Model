def collatz_len(n):
    cont = 0 
    while n>1:
        #print(n)
        if n&1:
            n = n + n + n + 1
        else:
            n//=2
        cont+=1
    return cont+1
top = 10 ** 6
print(max(range(2, top), key=collatz_len))