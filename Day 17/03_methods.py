# Instance method => Regular method - uses'self - works with instance variables - called using an object

class Student:
    def __init__(self, name):
        self.name = name

    def display(self):   # instance method
        print(self.name)

s = Student("Rishov")
s.display()

# Class method => Uses @classmethod - first parametre is cls - works with class variables 

class student:
    college='NSEC'

    @classmethod
    def change(cls,name):
        cls.college=name

student.change('IIT KGP')
print(student.college)



# static methods => uses @staticmethod - no self - no cls - Logic is related to the class - method doesn't depend on object or class state

class temp_convert:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
temp_inC= temp_convert()
res=temp_inC.celsius_to_fahrenheit(32)
print(res)


# Can a static method access instance variables?

# ❌ NO — directly it cannot

class Test:
    def __init__(self, x):
        self.x = x

    @staticmethod
    def show():
        print(self.x)   # ERROR


# correct way
class Test:
    def __init__(self, x):
        self.x = x

    @staticmethod
    def show(obj):
        print(obj.x)
