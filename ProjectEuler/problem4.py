def is_palindrome(n):
    return n==int(str(n)[::-1])
print(max([i*j for i in range(100,1000) for j in range(100,1000) if is_palindrome(i*j)]))
