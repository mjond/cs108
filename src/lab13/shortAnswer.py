'''short answer class
Models a short answer problem
Created Fall 2014
lab13
@author: smn4 
'''

from Problem import *

class ShortAnswer(Problem):
    def __init__(self, q, a):
        '''constructor and constructor to the parent class'''
        super().__init__(q)
        self.answer = a
              
    def ask_question(self):
        '''accessor'''
        return super().get_text() + '?'
    
    def check_answer(self, a):
        '''accessor'''
        return self.answer == a
    
    def get_answer(self):
        '''accessor'''
        return self.answer
    
    #tests
if __name__ == "__main__":
    q = ShortAnswer('question', 'answer')
    assert q.get_text() == 'question'
    assert q.get_answer() == 'answer'
    assert q.ask_question() == 'question?'
    assert not (q.check_answer('ans'))
    assert q.check_answer('answer')
    print('All ShortAnswer tests passed!')