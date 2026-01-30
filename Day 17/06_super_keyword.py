class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print('B')
        super().show()

class C(B):
    def show(self):
        print("C")
        super().show()


c=C()
c.show()


# super() moves forward in MRO, not upward in hierarchy.
# super() does NOT mean “call parent class directly”.
# Call the next class in the MRO list


# What is the Diamond Problem?
#      A
#     / \
#    B   C
#     \ /
#      D
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()
# java -> ignores multiple inh.
# c++ -> virtual keyword tomake single instance
# How does Python solve the Diamond Problem?

# Using MRO + C3 Linearization

print(D.__mro__) #D → B → C → A → object

d = D()
d.show()

# A is called once
# No ambiguity
# No duplicate execution
