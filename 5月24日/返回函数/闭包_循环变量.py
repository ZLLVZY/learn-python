def count():
    fs=[]
    def f(n):
        def g():
            return n*n
        return g
    for n in range(1,4):
        fs.append(f(n))
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())