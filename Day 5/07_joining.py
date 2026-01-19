# There are several ways to join, or concatenate, two or more lists in Python

# plus(+) operator => NO MUTATION
fruits=['orange', 'lemon', 'kiwi', 'lime']
extra=['apple','avocado']
print(fruits)
fruits=fruits+extra
print(fruits)


# extend() keyword
even=[0,2,4]
even.extend([6,8,10]) #solves the isssue in .append() method
print(even)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veg=fruits.extend(vegetables)
print(fruits_and_veg) # none
print(fruits) 
fruits.extend(vegetables)
fruits_and_veg = fruits

print(fruits_and_veg) #['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
