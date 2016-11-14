'''models a true false question
Created on Dec 4, 2014
lab13
@author: Mark Davis
'''

from Problem import *

class TrueFalse(Problem):
    '''True False class' constructor'''
    def __init__(self, q, a):
        super().__init__(q)
        if isinstance(a, bool) == False:
            raise TypeError ('boolean was false')
        else:
            self.answer = a
              
    def ask_question(self):
        '''accessor'''
        return super().get_text() + '\nIs this statement true or false?'
    
    def check_answer(self, a):
        '''accessor'''
        return str(self.answer) == a
    
    def get_answer(self):
        '''accessor'''
        return str(self.answer)