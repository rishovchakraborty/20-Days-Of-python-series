# Polymorphism means: One interface, multiple behaviors

print(len("Python"))
print(len([1, 2, 3]))
print(len((10, 20)))

class Test:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c   # overrides previous method

# Only the last definition exists.

# but we can stimulate an intution of polymorphism via DUCK TYPING

# What is Duck Typing?
# If it looks like a duck and quacks like a duck, it is a duck.

class Dog:
    def sound(self):
        print('Bark')

class Cat:
    def sound(self):
        print('meow')

class Animal:
    def make_sound(self,animal):
        animal.sound()

animal=Animal()
animal.make_sound(Cat())


# Operator Overloading in Python
# Python allows operators to behave differently for different objects using magic methods.

#  + -> __add__()
print(int.__add__(5,9)) # 14

# Custom operator overloading example:
class FloatAdd:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return FloatAdd(self.x+other.x,self.y+other.y)
    
p1=FloatAdd(5,1)
p2=FloatAdd(6,8)
p3=p1+p2
print(f'the result is = {p3.x}.{p3.y}')