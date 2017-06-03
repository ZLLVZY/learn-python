import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call %s()' % func.__name__)
        func(*args,**kw)
        print('end call %s()' % func.__name__)
    return wrapper
    
@log                          #now=log(now)
def now():
    print('2017-6-3')
f=now
f()
print(f.__name__)