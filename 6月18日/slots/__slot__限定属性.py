class Student(object):
    __slots__=('name','age')    #限制类的属性，子类的属性为自己的__slots__和父类的__slots__。
s=Student()
s.name='Zhang'
print(s.name)
s.score=100