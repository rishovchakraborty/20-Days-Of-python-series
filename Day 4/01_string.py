name = 'Rishov'
print(name)
print(type(name))
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)


#multiline string 
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)


first_name ='Rishov'
last_name='Chakraborty'
full_name=first_name+' '+last_name
print(full_name)
print(len(first_name) > len(last_name))


################
#string formatting 
#################

# using % operator
first_name ='Rishov'
last_name='Chakraborty'
dept='ECE'
formatted_str='my name is %s %s.I read in %s' %(first_name,last_name,dept)
print(formatted_str)

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision


rad=10
pi=3.14
area=pi * rad ** 2
formatted_str='the area of a circle having radius %d is %.3f' %(rad,area)
print(formatted_str)

python_libraries=['Django','Flask','Numpy']
formatted_str='the python libs are: %s'%(python_libraries)
print(formatted_str)

# new method-> String Interpolation 
shape='Circle'
rad=10
pi=3.14
area=pi * rad ** 2
formatted_str=f'the area of a {shape} with rad={rad} is : {area:.2f}'
print(formatted_str)


#unpacking characters
language='Python'
a,b,c,d,e,f=language
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n


# using indexing 
language='Python'
print(language[0],language[3]) #P h
print(language[-1],language[-6])


# slicing
language='Python'
first_three=language[0:3]  # starts at zero index and up to 3 but not include 3
print(first_three)
print(language[:len(language)])
print(language[-6:])

## reverse the string
language='Python'
print(language[::-1])

#skipping seq
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

#string methods
str='my name is Rishov'
print(str.capitalize())
# My name is rishov => Converts the first character of the string to capital letter and rest small

str='my name is Rishov'
print(str.count('r')) #0
print(str.count('R')) #1
print(str.count('i')) #2
print(str[9:])
print(str.count('i',9,12)) #1

# endswith(): Checks if a string ends with a specified ending 
str='my name is Rishov'
print(str.endswith('ov')) #true

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
str=' hy sjjk rtsh kdd'
sub_str='dd'
print(str.find(sub_str)) #15
print(str.index(sub_str)) #15

# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False


# isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True 
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True


# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False


# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False


# isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


str='khdh'
print(str.upper().lower())

# join(): Returns a concatenated string
web=['HTML', 'CSS', 'JavaScript', 'React']
res=' and '.join(web)
print(res) #HTML and CSS and JavaScript and React


# strip(): Removes all given characters starting from the beginning and end of the string
# speacially used to remove whitespaces
str=" hellow worls "
print(str)
print(str.strip())
print(str.strip().strip('hs'))
#  hellow worls 
# hellow worls
# ellow worl

# replace(): Replaces substring with a given string
challenge = 'Im a fond of python'
print(challenge.replace('python', 'coding'))

# split(): Splits the string
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False