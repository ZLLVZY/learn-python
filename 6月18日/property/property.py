'''
class Student(object):
    pass
s=Student()
s.score=9999                  直接暴露属性，不能检测是否符合
'''

'''
class Student(object):

    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be an integer!')
        if score<0 or score >100:
            raise ValueError('score must between 0 ~ 100!')
        else:
            self._score=score
            
    def get_score(self):
        return self._score
        
s=Student()
s.set_score(60)
s.get_score
s.set_score(101)
'''
class Student(object):

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be an integer!')
        if score<0 or score >100:
            raise ValueError('score must between 0 ~ 100!')
        else:
            self._score=score

        
s=Student()
s.score=60
s.score=101