from timeit import repeat

def rev1(s):
    if len(s) == 1:
        return s
    return s[-1] + rev1(s[:-1]) # slow

def rev2(s):
    return ''.join(reversed(s)) # simple faster

def rev3(s):
    return s[::-1] # even better


# test
for test in (rev1, rev2, rev3):
    print(test.__name__, min(repeat(stmt=lambda:test('qwertyuioplkjhgfdsazxcvbnm'), number=200000, repeat=3)))