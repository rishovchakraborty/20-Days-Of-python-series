# Magic methods (also called dunder methods) are special methods with double underscores:

# __method__


class Test:
    def __str__(self):
        return "Hello"

t = Test()
print(t)   # calls __str__()


# __new__() → creates object
#  __init__() → initializes object

class Demo:
    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")



class Greeting:
    def __call__(self, name):
        print(f"Hello {name}")

# Makes object behave like a function.
g = Greeting()
g("Rishov")   # looks like function call


class Test:
    def __del__(self): # destructor
        print("Object destroyed")
