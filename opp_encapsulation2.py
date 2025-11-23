# Python program to 
# demonstrate protected members 
class Base :
    def __init__ (self):
        # Protected member 
        self._a= 2

#creating a chils class
class dedrived :
    def __int__(self):
        Base.__init__(self)
        print("calling protected member of base class :", self._a)

        # Modify the protected variable: 
        self._a = 3
        print("calling modified procted member of base class:",self._a)


obj1 = dedrived() #child class er obj

obj2 = Base()  #parent class er obje
# Accessing the protected variable outside 
print("Accessing protected member of obj2: ", obj2._a) 


