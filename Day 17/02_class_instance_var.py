class Student:
    college = "NSEC"      # class variable => shared by all objects and only one copy in the memory ... can be accessed via class name 

    def __init__(self, name):
        self.name = name  # instance variable ...uses self...unique to each object ...acces via obj


# Python stores instance variables in a dictionary called __dict__ inside each object.

s = Student('Rishov')
print(s.__dict__) # {'name': 'Rishov'}

# Where are class variables stored?

# In the class’s __dict__
print(Student.__dict__)



class Employee:
    company='TCS' # class variables

e1= Employee()
e2= Employee()

e1.company='Google' # instance variable will be created

print(e1.company)
print(e2.company)
print(Employee.company)
# Google
# TCS
#  TCS

# steps =>
# e1.company → instance variable created..separate dict
# Class variable remains unchanged
# Only that object is affected

Employee.company='CTS'
print(e1.company)
print(e2.company)
print(Employee.company)

# Google
# CTS
# CTS
