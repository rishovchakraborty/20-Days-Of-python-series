# Showing only essential features and hiding implementation details

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Abstraction         	                Encapsulation
# Hides implementation	                Hides data
# Focus on design	                    Focus on data protection
# Achieved using abstract classes    	Achieved using private variables
# What to do                           	How to protect


# An abstract class:
# Cannot be instantiated
# Contains one or more abstract methods
# Acts as a blueprint

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass

# Any subclass must implement start().

# abc stands for:
# Abstract Base Classes

# @abstractmethod =>
# It forces subclasses to implement the method

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    pass

d = Dog()
# TypeError: Can't instantiate abstract class



from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def desc(self):
        print('its a shape')

class Circle(Shape):
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return 3.14 * self.rad * self.rad
    
c=Circle(5)
print(c.area())
c.desc()