x = 5 # Assigns the value 5 to the variable x

# Operator 	    Name	            Example	            Same As
# +=	Addition Assignment 	    x += 3	            x = x + 3
# -=	Subtraction Assignment	    x -= 3	            x = x - 3
# *=	Multiplication Assignment	x *= 3	            x = x * 3
# /=	Division Assignment	        x /= 3	            x = x / 3
# %=	Modulus Assignment	        x %= 3	            x = x % 3
# //=	Floor Division Assignment	x //= 3	            x = x // 3
# **=	Exponent Assignment	        x **= 3	            x = x ** 3
# &=	Bitwise AND Assignment	    x &= 3	            x = x & 3
# `	=`	Bitwise OR Assignment	    `x
# ^=	Bitwise XOR Assignment	    x ^= 3	            x = x ^ 3
# >>=	Right Shift Assignment	    x >>= 3         	x = x >> 3
# <<=	Left Shift Assignment	    x <<= 3	            x = x << 3

# The Walrus Operator (:=) 
# Introduced in Python 3.8, the "walrus operator" allows assignment within an expression. This can make code more concise, particularly within loops and comprehensions, by letting you assign a value to a variable and use that value in the same condition/expression. 

# Example of the walrus operator in a while loop
# Assigns the length of 'a' to 'n' and checks if n is greater than 2
a = [1, 2, 3, 4, 5]
while (n := len(a)) > 2:
    print(f"List length is {n}. Removing an element.")
    a.pop()
# Output:
# List length is 5. Removing an element.
# List length is 4. Removing an element.
# List length is 3. Removing an element.
