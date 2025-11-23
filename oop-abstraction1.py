
from abc import ABC , abstractmethod

class shape (ABC) :
    @abstractmethod
    def area (self) :
        pass

class circle (shape ):
    def __init__(self,radius):
        self.radius = radius

    def area (self):
        return 3.14 * self.radius * self.radius


my_shape = shape()     
my_circle = circle(5)
print("circle area :",my_circle.area())
