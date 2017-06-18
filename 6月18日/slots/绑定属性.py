class Student(object):
    pass
s=Student()
s.name='Zhang'
print(s.name)
def set_age(self,age):
    self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)
s2=Student()                 #s2.set_age(26)
Student.set_age=set_age      #error
s2.set_age(26)               #一个实例的方法对另一个不起作用，对类才可以
print(s2.age)