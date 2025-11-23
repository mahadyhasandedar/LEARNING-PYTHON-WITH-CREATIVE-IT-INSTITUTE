class Base: #parent class
    def __init__(self): #constructor
        self.a = "python" #public
        self.__b = "language" #private
#creating a child class

class dedrived (Base):
    def __init__(self):
        Base.__init__(self)
        print("calling private member of base class :")
        print(self.a)
        #print(self.__c)

obj1= Base()
obj2= dedrived()
