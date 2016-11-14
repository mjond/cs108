'''Game of War simulator
homework08
Created Fall 2014
@author Mark Davis
'''

import random

class Card:
    '''models the card game war
    Invariants:
        Card number is 1 to 13 inclusive
        Card suits are diamond, heart, club and spade 
    '''
    #setting up the constructor
    def __init__(self):
        ''' Card Game Constructor '''
        self._card_num = random.randint(2,14)
        self._suit = random.randint(1,4)
    
    #accessors
    def get_suit(self):
        '''accessor for spades'''
        return self._suit
    def get_card_num(self):
        '''accessor for card number'''
        return self._card_num
    
    #comparisons
    def __gt__(self, other):
        if self._card_num == 1:
            return True
        elif other._card_num == 1:
            return False
        elif self._card_num > other._card_num:
            return True
        else:
            return False
    #more comparisons  
    def __lt__(self, other):
        if self._card_num == 1:
            return True
        elif other._card_num == 1:
            return False
        elif self._card_num < other._card_num:
            return False
        else:
            return True
    
    def __eq__(self, other):
        if self._card_num == other._card_num:
            return False
        
    #the string method for printing out the random cards      
    def __str__(self):
        
        symbol = ''
        rank = ''
        
        # getting the correct format for queen, jack, king and ace
        if self._card_num == 11:
            symbol = 'J'
        elif self._card_num == 12:
            symbol = 'Q'
        elif self._card_num == 13:
            symbol = 'K'
        elif self._card_num == 14:
            symbol = 'A'
        else:
            symbol = str(self._card_num)
        # getting the correct format for the suit
        if self._suit == 1:
            rank = 'H'
        elif self._suit == 2:
            rank = 'D'
        elif self._suit == 3:
            rank = 'S'
        elif self._suit == 4:
            rank = 'C'
            
        return (symbol + rank)
            
   
    
#-------main code--------
#making a list for each hand
hand1 = []
hand2 = []
#adding cards to hand 1
print('Hand 1')
for i in range(5):
    hand1.append(Card())
for i in hand1:
    print(i)
#adding cards to hand 2
print('Hand 2')
for i in range(5):
    hand2.append(Card())
for i in hand2:
    print(i)

#keeping track of the amount of wins
player1_wins = 0
player2_wins = 0

#calculating wins and losses        
if hand1[0] > hand2[0]:
    player1_wins += 1
else:
    player2_wins += 1
    
if hand1[1] > hand2[1]:
    player1_wins += 1
else: 
    player2_wins += 1
    
if hand1[2] > hand2[2]:
    player1_wins += 1
else:
    player2_wins += 1
    
if hand1[3] > hand2[3]:
    player1_wins += 1
else:
    player2_wins += 1
    
if hand1[4] > hand2[4]:
    player1_wins += 1
else:
    player2_wins += 1


#determining who has the most wins and printing out the winner
if player1_wins > player2_wins:
    print('Player 1 wins with %d wins' % player1_wins)
elif player1_wins == player2_wins:
    print("It's a draw")
else:
    print('Player 2 wins with %d wins' % player2_wins)
