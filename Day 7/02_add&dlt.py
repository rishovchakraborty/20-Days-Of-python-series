fruits = {'banana', 'orange', 'mango', 'lemon'}

fruits.add('lime')
print(fruits)

fruits.add({'lime','apple'}) #error

# All elements inside a set must be hashable (immutable)

# Hashable types ✅

# int

# float

# str

# tuple (if it contains only hashable items)

# frozenset

# Unhashable types ❌

# list

# set

# dict

# Why?
# Because mutable objects can change → hash would change → set breaks.


# Add multiple items at once (BEST)
fruits.update({'lime', 'apple'})
fruits.update(['lime', 'apple'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)


# Removing Items from a Set 

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

# If we want to clear or empty the set we use clear method.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()


# If we want to delete the set itself we use del operator.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st


# conversion set <-> list
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}