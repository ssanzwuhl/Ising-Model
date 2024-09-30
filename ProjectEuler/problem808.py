def is_prime(n: int):
    if not n&1:
        return False
    if n<=3:
        return True
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i==0:
            return False
    return True

def is_palindrome(n: int):
    assert type(n)


