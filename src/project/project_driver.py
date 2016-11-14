'''Final Project: Dodging Game - driver program
Created Fall 2014
Final Project
@author: Mark Davis (mjd85)
'''

from tkinter import *
from big_square import *
from small_square import *
import random
from user import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

class Driver:
    def __init__(self):
        '''constructor
        
        '''
        self.window = Tk()
        self.window.title('Dodge the Blocks!')
        
        '''the canvas where the game will occur'''
        self.canvas = Canvas(self.window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg = 'white')
        self.canvas.pack()
        
        #making the frame
        frame = Frame(self.window)
        frame.pack()
        
        #instructions label
        inst_lb = Label(frame, text = 'Use the arrow keys to \n control the blue block')
        inst_lb.grid(row = 1, column = 1, sticky = E)
        
        frame2 = Frame(frame)
        frame2.grid()
        
        #"Score" label
        sc_lb = Label(frame2, text = 'Score:')
        sc_lb.grid(row = 3, column = 4, sticky = W)
        #score counter
        self.score_count = StringVar()
        score = Label(frame2, textvariable = self.score_count)
        score.grid(row = 3, column = 5, sticky = W)
        
        #label for directions for the user
        inst_lb = Label(frame2, text = 'Choose a difficulty:')
        inst_lb.grid(row = 2, sticky = E)
        
        #quit button. When clicked, closes the window
        self.terminate = False
        quit_bt = Button(frame2, text = 'Quit', command = self.quit)       
        quit_bt.grid(row = 3, column = 2, sticky = W)
        
        #start button. When clicked, the game will start and will then become the pause button
        self.isStopped = True
        self.start = StringVar()
        self.start.set('Start')
        start_bt = Button(frame2, textvariable = self.start, command = self.start_pause_game)
        start_bt.grid(row = 3, column = 3, sticky = W)
        
        #restart button, resets the game so it can be played again
        restart_bt = Button(frame2, text = 'Restart', command = self.restart)
        restart_bt.grid(row = 3, column = 3, sticky = E)
        
        #easy difficulty button
        easy_bt = Button(frame2, text = 'Easy', command = self.easy)
        easy_bt.grid(row = 2, column = 1, sticky = E)
        
        #hard difficulty button
        hard_bt = Button(frame2, text = 'Hard', command = self.hard)
        hard_bt.grid(row = 2, column = 2)
        
        #Chuck Norris mode
        chuck_bt = Button(frame2, text = 'Chuck Norris Mode', command = self.chuckNorris)
        chuck_bt.grid(row = 2, column = 3, sticky = W)
        
        #GAME OVER LABEL
        self.game_over = StringVar()
        over_lb = Label(frame2, textvariable = self.game_over)
        over_lb.grid(row = 4, column = 2)
        
        #creating a list for the big squares
        self.biglist = []
        self.biglist.append(Square())#putting a square into the list so the animate loop will have something to work with from the start
        
        self.smallList = []
        self.smallList.append(SmallSquare())
        
        #binding the user controls to the arrow keys, code is inspired by the class demo: LinesWithArrows
        self.us = User()
        self.us.create_user(self.canvas)
        self.canvas.bind('<Left>', self.processLeft)#binding the arrow key controls to the game
        self.canvas.bind('<Right>', self.processRight)
        self.canvas.bind('<Up>', self.processUp)
        self.canvas.bind('<Down>', self.processDown)
        self.canvas.focus_set()
        
        #variable for the score label
        self.scorer = 0
        
        #starting the animation
        self.animate()
        self.window.mainloop()
        
    def quit(self):
        '''terminates the program and closes the window'''
        self.terminate = True
        self.window.destroy()
        
    def start_pause_game(self):
        '''starts the game when the 'start' button is clicked, then becomes the 
        'pause' button and will pause the game'''
        if self.isStopped == True:
            self.isStopped = False
            self.start.set('Pause')
            self.animate()
        else:
            self.isStopped = True
            self.start.set('Start')      
        
    def animate(self):
        '''animate loop
        when the game isn't paused, it'll produce squares'''
        self.bigcounter = 0 
        self.smallcounter = 0
        
        while self.isStopped == False:
            self.canvas.delete(ALL) #deleting everything so there isn't any smudge
            self.us.create_user(self.canvas) #creating the user's square
            
            for i in self.biglist: # a list for the big squares
                i.move()#it goes through each square in the list and moves and renders them
                i.render(self.canvas)
                
            for m in self.smallList:#a list for the small squares
                m.move()#it goes through each square in the list and moves and renders them
                m.render(self.canvas)
            
            self.bigcounter += 1 #a counter for when to put in another big square
            if self.bigcounter == self.big_num_count:# if the counter reaches a certain number, another square with random coordinates will be appended to the list
                x = random.randint(0,WINDOW_WIDTH - 30)
                self.biglist.append(Square(x, 0, x + 30, 30, fill = 'red'))
                self.bigcounter = 0#counter is reset to 0
                
            self.smallcounter += 1# counter for when to put in another small square
            if self.smallcounter == self.small_num_count:#if the counter raches a certain number, another square with random coordinates and the counter is reset to 0
                n = random.randint(0, WINDOW_WIDTH - 30)
                self.smallList.append(SmallSquare(n, 585, n + 15, 600, fill = 'orange'))
                self.smallcounter = 0
                
            copy_big = self.biglist[:]#making a copy of the big square list
            for i in copy_big: #goes through the copied list 
                if i.get_y() > 600: #if the coordinates are off the screen, it removes it from the list and score goes up 1
                    self.scorer += 1
                    self.biglist.remove(i)
                    
            copy_small = self.smallList[:]#making a copy of the small square list
            for b in copy_small:#goes through the list
                if b.get_y2() < 0:#if the coordinates are off the screen, removes it from the list and score goes up 1
                    self.scorer += 1
                    self.smallList.remove(b)
                    
            self.score_count.set(str(self.scorer))#updating the score label
                            
            
            px1 = self.us.get_x() #making points for the user's square
            py1 = self.us.get_y()
            
            px3 = self.us.get_x2()
            py3 = self.us.get_y2()
           
            
            for j in self.biglist:#going through the big square list and making points for the corners
                y1 = j.get_y()                              #1  #2
                x1 = j.get_x()                              #4  #3
                x3 = j.get_x2()
                y3 = j.get_y2()
                
                ''' compares the corners to the user square's corners. If they are within each other, that means the user hit a falling block'''
                if (px1 <= x3 <= px3) and (py1 <= y3 <= py3): #case 1 
                    self.isStopped = True
                    self.game_over.set('GAME OVER')
                elif (py1 <= y1 <= py3) and (px1 <= x1 <= px3): #case 3
                    self.isStopped = True
                    self.game_over.set('GAME OVER')
                elif (px1 <= x1 <= px3) and (py1 <= y3 <= py3): #case 4
                    self.isStopped = True
                    self.game_over.set('GAME OVER')
                elif (py1 <= y1 <= py3) and (px1 <= x3 <= px3): #case 2
                    self.isStopped = True
                    self.game_over.set('GAME OVER')
                    
            for m in self.smallList: #going through the big square list and making points for the corners
                y1 = m.get_y()
                x1 = m.get_x()
                x3 = m.get_x2()
                y3 = m.get_y2()
                    
                ''' compares the corners to the user square's corners. If they are within each other, that means the user hit a falling block'''
                if (px1 <= x3 <= px3) and (py1 <= y3 <= py3): #case 1
                    self.isStopped = True
                    self.game_over.set('GAME OVER')
                elif (py1 <= y1 <= py3) and (px1 <= x1 <= px3): #case 3
                    self.isStopped = True
                    self.game_over.set('GAME OVER')
                elif (px1 <= x1 <= px3) and (py1 <= y3 <= py3): #case 4
                    self.isStopped = True
                    self.game_over.set('GAME OVER')
                elif (py1 <= y1 <= py3) and (px1 <= x3 <= px3): #case 2
                    self.isStopped = True
                    self.game_over.set('GAME OVER')
                                        
            self.canvas.after(self.update)#updating the canvas after a certain time, depending on the difficulty
            self.canvas.update()                                        
            
    def processLeft(self, event):
        '''moves the user square left'''
        self.us.moveLeft(self.canvas)
        
    def processRight(self, event):
        '''moves the user square right'''
        self.us.moveRight(self.canvas)
        
    def processDown(self, event):
        '''moves the user's square down'''
        self.us.moveDown(self.canvas)
        
    def processUp(self, event):
        '''moves the user square up'''
        self.us.moveUp(self.canvas)
        
    def easy(self):
        '''setting the easy difficulty
        the counter for the animate is 20, therefore less blocks to be made over more time'''
        self.big_num_count = 25
        self.small_num_count = 40
        self.update = 30
        
    def hard(self):
        '''setting the hard difficult
        animation counter is set to 10, therefore more blocks to be made'''
        self.big_num_count = 20
        self.small_num_count = 30
        self.update = 15
        
    def chuckNorris(self):
        '''chuck norris mode'''
        self.big_num_count = 3 
        self.small_num_count = 15
        self.update = 20
    
    def restart(self):
        '''for the restart button
        resets the game to be played again without having to crash the program and having to run it again'''
        self.isStopped = True
        Driver()
        
        if self.isStopped == False:
            self.animate()
            
        
Driver()

