x = 5
y = 5.7
z = 2 + 3j

print(type(x))  # ➜ <class 'int'>
print(type(y))  # ➜ <class 'float'>
print(type(z))  # ➜ <class 'complex'>


x = "24"
print(type(x))    # ➜ <class 'str'>

x = int(x)
print(type(x))    # ➜ <class 'int'>
print(x * 3)      # ➜ 72

x = 3.14
print(int(x))     # ➜ 3

x = 3
print(float(x))   # ➜ 3.0

x = 3      # real part
y = 4      # imaginary part
print(complex(x, y))  # ➜ (3+4j)


import math

price = 35.54879865

print(round(price))        # ➜ 36 (nearest whole number)
print(round(price, 2))     # ➜ 35.55 (2 decimal places)
print(round(price, 1))     # ➜ 35.5

print(math.floor(price))   # ➜ 35 (round down)
print(math.ceil(price))    # ➜ 36 (round up)
print(math.trunc(price))   # ➜ 35 (truncate decimal part)
print(int(price))    


import random

print(random.random())       # ➜ Random float between 0 and 1
print(random.randint(1, 6))  # ➜ Simulates a dice roll (1 to 6)

x = 70.4
print(isinstance(x, int))    # ➜ False
print(isinstance(x, float))  # ➜ True
