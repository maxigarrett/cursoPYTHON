from functools import reduce


def fact(n):
    return reduce(lambda x,y:x*y, range(2,n+1), 1)
print(fact(4))