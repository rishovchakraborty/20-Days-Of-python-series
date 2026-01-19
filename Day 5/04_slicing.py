fruits = ['banana', 'orange', 'mango', 'lemon']

# Positive Indexing
all_fruits=fruits[0:len(fruits)]
print(all_fruits)
print(fruits[0:])
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
banana_mango = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
orange_lemon = fruits[1::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
print(banana_mango)
print(orange_lemon)

#negetive indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
# reverse printing with a negetive step
reverse_fruits=fruits[::-1]
print(reverse_fruits)

