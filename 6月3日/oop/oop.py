class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score
        
    def print_score(self):
        print('%s: %s' % (self.name,self.score))

ZY=Student('ZY',100)
ZL=Student('ZL',99)
ZY.print_score()
ZL.print_score()

