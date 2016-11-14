'''solar system
lab10
cfreated fall 2014
@author Mark Davis (mjd85)
'''
  
 
from sun import Sun
from planet import Planet

class Solar_System:
    
    def __init__(self):
        self._sun = None
        self._planets = []
        
                
    def add_sun(self, a_sun):
        if isinstance(a_sun, Sun):
            self._sun = a_sun
        else:
            raise TypeError('add_sun(): cannot add ' + str(type(a_sun)) + ' to solar system')

    def add_planet(self, a_planet):
        if isinstance(a_planet, Planet):
            self._planet = a_planet
        else:
            raise TypeError('add_planet(): cannot add ' + str(type(a_planet)) + ' to solar system')
        
    def show_planets(self):
        for a_planet in self._planets:
            print(a_planet)

            
    def show_sun(self):
        for a_sun in self._sun:
            print(a_sun)    



if __name__ == '__main__':      
        
    try:
        solSys1 = Solar_System()
        solSys1.add_sun('porcupine')
        print(solSys1)
    except TypeError as ve:
        print('Dealt with TypeError:', ve)

    try:
        solSys2 = Solar_System()
        sunny4 = Sun('Mayonnaise', 5, 14, 3, 23, 'yellow')
        solSys2.add_sun(sunny4)
        print(solSys2)
    except TypeError as ve:
        print('Dealt with TypeError:', ve)
        
    try:
        solSys3 = Solar_System()
        solSys3.add_planet('pineapple')
        print(solSys3)
    except TypeError as ve:
        print('Dealt with TypeError:', ve)    
    
    try:
        solSys4 = Solar_System()
        planet4 = Planet('Pedro', 5, 2, 5, 'red')
        solSys4.add_planet(planet4)
        print(solSys4)
    except TypeError as ve:
        print('Dealt with TypeError:', ve)    
    
    
        
        