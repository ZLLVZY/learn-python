class Student(object):
    def __init__(self):
        self.name='ZL'
    def __getattr__(self,attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
s=Student()
print(s.name)
print(s.score)
print(s.age())