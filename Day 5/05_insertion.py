# List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0]='avacado'
print(fruits) #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1]='apple'   #  ['avocado', 'apple', 'mango', 'lemon']


#checking a item in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
is_exist= 'orange' in fruits  #true
is_exist= 'apple' in fruits   #false
print(is_exist)

#Adding An Item
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append(['lime','watermalon'])
print(fruits)
fruits.append('lime','watermalon') #error -> cant pass >1 obj
# list.append() takes exactly one argument (2 given)

#  insert() method to insert a single item at a specified index
# syntax
# lst = ['item1', 'item2']
# lst.insert(index, item)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)