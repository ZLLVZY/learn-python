from functools import reduce
def f1(a,b):
    return a*10+b
def f2(a,b):
    return a/10+b/10
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}[s]
def str2float(s):
    n=0
    for c in s:
        if '.'==c:
            break;
        n=n+1
    s1=s[:n]
    k=0
    s2=['0']
    while k<(len(s)-n-1):
        k=k+1
        i=-1*k
        s2.append(s[i])
    e1=reduce(f1,map(char2num,s1))
    e2=reduce(f2,map(char2num,s2))
    return (e1+e2)