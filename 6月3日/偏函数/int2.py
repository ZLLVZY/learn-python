import functools
int2=functools.partial(int,base=2)
print(int2('1001'))


#def int2(x,base=2):
    #return int(x,base)