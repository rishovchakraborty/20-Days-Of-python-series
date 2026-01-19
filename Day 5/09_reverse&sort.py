fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[::-1]) # backward read

fruits.reverse() # reversing in place
print(fruits)


# To sort lists we can use sort() method or sorted() built-in functions.

# sort(): this method modifies the original list
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending


ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)


# sorted(): returns the ordered list without modifying the original list 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']