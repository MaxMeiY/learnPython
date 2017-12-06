from functools import reduce
def r_f(n):
    if n == 1:
        return n
    return n * r_f(n-1)

def c_f(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

def i_f(n):
    ans = 1
    while n > 1:
        ans = ans * n
        n -= 1

    return ans

def l_f(n):
    import math
    return math.factorial(n)


# Tests
print(r_f(6), c_f(6), i_f(6), l_f(6))
print(r_f(500)==c_f(500)==i_f(500)==l_f(500))

from timeit import repeat
for test in (r_f,c_f,i_f,l_f):
    print(test.__name__, min(repeat(stmt=lambda: test(500), number=20, repeat=3)))