name='rishov'
print(type(name))  # <class 'str'>
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'rishov'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip


#casting
# int to float
num_int=10
print(num_int) #10
num_float= float(num_int)
print(num_float) #10.0

# float to int
gravity=9.8
print(int(gravity))

# int to str
ph_no=9123321231
print(type(str(ph_no)))


# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

name='deepak'
print(name)
name_list=list(name)
print(name_list)