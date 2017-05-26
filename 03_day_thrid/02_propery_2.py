#coding=UTF-8

#Python内置的@property装饰器就是负责把一个方法变成属性调用的

class Student(object):
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
            
        
S=Student()

S.score=60 #实际转换为S.set_score(60)

print(S.score)#实际转换为S.get_score()        