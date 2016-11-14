'''quiz class
Created Fall 2014
lab13
@author: smn4
'''

from shortAnswer import ShortAnswer
from FillintheBlank import FillBlank
from TrueFalse import TrueFalse
import random

class Quiz:
    def __init__(self):
        self.problems = []
        #putting questions into the list
        self.problems.append(ShortAnswer('Where were the olympics held in 1956', 'Melbourne'))
        self.problems.append(ShortAnswer('What is the hottest recorded temperature in the United States', '134'))
        self.problems.append(ShortAnswer('What is the capital of Canada', 'Ottawa'))
        self.problems.append(FillBlank('Calvin College is in _______', 'Grand Rapids'))
        self.problems.append(TrueFalse('You are in computer science class', True))
        #randomizing the questions
        random.shuffle(self.problems)
        
        self.problemNum = 0
        
    def ask_current_question(self):
        '''accessor'''
        return self.problems[self.problemNum].ask_question()
    
    def get_current_answer(self):
        '''accessor'''
        return self.problems[self.problemNum].get_answer()
    
    def check_current_answer(self, answer):
        '''accessor'''
        return self.problems[self.problemNum].check_answer(answer)
    
    def has_next(self):
        '''setting the counter'''
        return self.problemNum < len(self.problems) - 1
    
    def next(self):
        '''when there are no more problems, raise the error'''
        if self.problemNum == len(self.problems) - 1:
            raise Exception("There are no more problems")
        self.problemNum += 1
    
    
        