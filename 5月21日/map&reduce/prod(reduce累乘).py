from functools import reduce
def c(a,b):
    return a*b
def prod(L):
    return reduce(c,L)
print('3*5*7*9=%s' % prod([3,5,7,9]))