# Object-Oriented Programming (OOP) is a programming paradigm where we design programs using objects that represent real-world entities.

# Data → variables (attributes)
# Behavior → functions (methods)

class Car:
    speed = 90 # value / attributes / data
    def start(self): # behavior or methods
        print("Car started")

my_car = Car()  # object
my_car.start()

# self => in python it refers to current object  (similar to this keyword inother language but there this works internally , here we need to pass it ....like a connection)

# Differentiate between class variables and instance variables

class Person:
    name=''
    def say_name(self,name):
        self.name=name
        print(self.name)

p= Person()
p.say_name("rishov")



# In Python:
# Object is created by __new__()
# __init__() only initializes the already created object

class Demo:
    def __init__(self):
        print("Object initialized")

d = Demo()
