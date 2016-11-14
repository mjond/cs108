'''driver program
Created Fall 2014
lab13
@author: smn4
'''

from tkinter import *
from quiz import Quiz

class Controller:
    def __init__(self):
        self.window = Tk()
        self.window.title('Simple Quiz')
        
        self.quiz = Quiz()
        #setting the text box 
        self.question_text = Text(self.window, font="arial 16", width = 40, height = 4, wrap = WORD)
        self.question_text.insert(1.0, self.quiz.ask_current_question())
        self.question_text.pack()
        #making the text entry and binding the 'enter' button to it
        self.answer = StringVar()
        self.answerEntry = Entry (self.window, textvariable = self.answer)
        self.answerEntry.pack(side = LEFT)
        self.answerEntry.focus_set()
        self.answerEntry.bind("<Return>", self.check_answer)
        #label
        self.instructions = StringVar()
        self.instructions.set('\u21D0 Enter your answer here')
        self.instrLabel = Label(self.window, textvariable = self.instructions)
        self.instrLabel.pack(side = LEFT)
        
        self.window.mainloop()
        
    def check_answer(self, event):
        if self.quiz.check_current_answer(self.answer.get()):
            #Got it right!!
            self.instructions.set("Good job!  Next question ...")
        else:
            self.instructions.set("Sorry, the answer was " + self.quiz.get_current_answer()) 
        self.answer.set('')
        
        #Go to the next question if it exists
        self.question_text.delete(1.0, END)  
        if (self.quiz.has_next()):
            self.quiz.next()
            self.question_text.insert(1.0, self.quiz.ask_current_question())
        else:  
            self.question_text.insert(1.0, 'Sorry, there are no more questions.')#when there are no more questions to be asked
            self.answerEntry.configure(state='disabled')
   
Controller()
