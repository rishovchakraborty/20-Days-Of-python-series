# like C++ or JAVA , we do not have any traditional PRIVATE variable concepts in python

# instead we have NAMING CONVENTIONS & NAME MANGLING


# _var → Protected by convention 
class Demo:
    def __init__(self):
        self._age = 21

# means : internal use only - accessed in subclasses

# __var → Private via name mangling
class Demo:
    def __init__(self):
        self.__salary = 50000

d=Demo()
print(d.__salary) # error
print(d.__dict__) # {'_Demo__salary': 50000}
# Python doesn’t support true private variables
print(d._Demo__salary) # 50000
# Python changes the name internally
# Prevents accidental access
# Avoids name clashes in inheritance


# __var__ → Special / magic variables
# Reserved for Python internals
# Example: __init__, __str__, __dict__
