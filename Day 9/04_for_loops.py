nums=[0,1,2,3,4,5]

for num in nums:  # number is temporary name to refer to the list's items, valid only inside this loop
    print(num,end=' ')



language='Python'
res=[]
for letter in language:
    res.append(letter)

print(' '.join(res))

language='java'
for i in range(len(language)):
    print(language[i],end='')




languages = ['Python', 'Java', 'Cplusplus', 'Go', 'Rust', 'AI']
res=[]

for lang in languages:
    res.append(lang[:2])
print(' '.join(res))


#tuple
nums=(1,2,3,4,5,6)
for num in nums:
    print(num+1,end=' ')


nums=(1,2,3,4,5,6)
for i in range(len(nums)):
    print(nums[i],end=' ')


#set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

#dict
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

for key in person:
    print(key)

for key, value in person.items():
    print(f"{key} : {value}")



lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]



# syntax nested loops
# for x in y:
#     for t in x:
#         print(t)


# for else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)


for number in range(6):
    pass