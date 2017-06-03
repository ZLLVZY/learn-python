import functools
def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper1(*args,**kw):
                print('%s %s()' % (text,func.__name__))
                return func(*args,**kw)
            return wrapper1
        return decorator
    else:
        @functools.wraps(text)
        def wrapper2(*args,**kw):
            print('call %s()' % text.__name__)
            return text(*args,**kw)
        return wrapper2
@log             #@log('execute')
def now():
    print('2017-6-3')
f=now
f()