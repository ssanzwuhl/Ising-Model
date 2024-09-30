def fib_index_len(n):
    a, b = 0, 1
    while n>1:
        a, b = b, b + a
        n-=1
    return len(str(a))
top = 1000
iterator = 0
while fib_index_len(iterator)<top:
    iterator+=1
print(iterator-1)