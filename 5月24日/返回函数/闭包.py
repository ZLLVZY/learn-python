def count():
    fs=[]
    for n in range(1,4):
        def f():
            return n*n
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())