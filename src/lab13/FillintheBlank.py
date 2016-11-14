'''models a fill in the blank question
Created on Dec 4, 2014
lab13
@author: Mark Davis (mjd85)
'''

from Problem import *

class FillBlank(Problem):
    '''Fill in the blank type - constructor'''
    def __init__(self, q, a):
        super().__init__(q)
        self.answer = a
              
    def ask_question(self):
        '''accessor'''
        return super().get_text() + '\nFill in the blank.'
    
    def check_answer(self, a):
        '''accessor'''
        return self.answer == a
    
    def get_answer(self):
        '''accessor'''
        return self.answer