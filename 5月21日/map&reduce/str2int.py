from functools import reduce
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def fn(x,y):
    return x*10+y
	
def str_to_int(L):
    return reduce(fn,map(char2num,L)) 