def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
    
@log('execute')                        #now=log('execute')(now)
def now():
    print('2017-6-3')
f=now
f()
print(f.__name__)