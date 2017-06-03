def log(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper
    
@log                          #now=log(now)
def now():
    print('2017-6-3')
f=now
f()
print(f.__name__)