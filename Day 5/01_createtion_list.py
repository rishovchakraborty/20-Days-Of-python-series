# A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

#creation 
demo0=list() ##empty list
demo=list((1,2,3))
demo2=list([4,5,6])
print(demo2)
print(len(demo))

demo3=list(range(1,5))
print(demo3)

#using sq brackets
list_demo=[]

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 
personal_info=['Rishov',21,False,{'dept':'ece','cgpa':8.3}]
print('given data are: ',personal_info)
print('the name is : ',personal_info[0])
