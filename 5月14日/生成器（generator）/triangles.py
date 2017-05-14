def triangles(max=10):
    n=0
    L=[1]
    while n<max:
        yield L
        if 0!=n:
            L2=L[:]
            for i in range(1,n+1):
                L[i]=L2[i-1]+L2[i]
        L.append(1)
        n=n+1
for x in triangles():
    print(x)