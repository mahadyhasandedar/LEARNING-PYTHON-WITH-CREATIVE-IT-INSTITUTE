from abc import ABC , abstractmethod
class polygon (ABC):
    def sides (self):
        pass

class Triangle (polygon):
    def sides (self):
        print("3 sides")

class Penta (polygon):
    def sides (self):
        print("5 sides")

class Hexa (polygon):
    def sides (self):
        print("6 sides")

t=Triangle ()
t.sides()

p= Penta ()
p.sides()

h= Hexa ()
h.sides()
