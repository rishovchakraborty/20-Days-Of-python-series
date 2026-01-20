# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# creation
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


person= {
    'Name' : 'Rishov',
    'age' : 21,
    'country' : 'India',
    'address' : 'Kolkata',
    'Skill' : ['c++','react','js','python'],
    'contact': {
        'mobile':'6856546',
        'email':'abc@gmail.com'
    }
}

#add intems
person['job_title'] = 'Instructor' #added 
# person['skills'].append('HTML') #error as skills not present

print(person)
print(len(person))

# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.

print(person['education']) #error as key doesnt exist
print(person.get('education')) #None
print(person.get('country')) # India


#remove
person.pop('Name') 
del person['Name']
person.popitem() #last key removed
del person


# syntax for getting keys as list
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# syntax for getting values as a list
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])