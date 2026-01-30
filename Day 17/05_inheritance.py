# types
# 1. single inheritance

class A:
    pass
class B(A):
    pass

# 2. Multilevel Inheritance
class A:
    pass

class B(A):
    pass

class C(B):
    pass

# 3. Hierarchical Inheritance
class A:
    pass

class B(A):
    pass

class C(A):
    pass

# 4. Multiple Inheritance
class A:
    pass

class B:
    pass

class C(A, B):
    pass



# What is Multiple Inheritance?
# A class inheriting from more than one parent class
class Father:
    def skill(self):
        print('Driving')

class Mother:
    def skill(self):
        print('cooking')

class child(Father,Mother):
    pass

c=child()
c.skill() # Driving

#  Which skill() gets called?
#  That’s where MRO comes in.

# METHOD RESOLUTION ORDER => the order in which python searches for a method -> using C3 Linearization algorithm.

print(child.__mro__)
''' (
 <class '__main__.child'>,
 <class '__main__.Father'>, 
 <class '__main__.Mother'>,
 <class 'object'>)
'''


