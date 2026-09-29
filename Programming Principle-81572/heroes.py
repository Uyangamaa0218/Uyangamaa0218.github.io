from abc import ABC
from interfaces import IFly

class Being(ABC):
    pass

class Superhero(Being):
    pass

class Humanhero(Superhero):
    pass

class Batman(Humanhero, IFly):
    def fly(self):
        print("I'm flying with my bat wings!")
    def land(self):
        print("I'm landing safely on the ground.")
