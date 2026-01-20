a=0
if a>0:
    if a%2==0:
        print(' a is pos and even')
    else:
        print('pos not even')
elif a==0:
    print('a is zero')
else:
    print('a is negative')


# We can avoid writing nested condition by using logical operator 'and'

#and
a=109
if a>0 and a%2==0 :
    print('a is pos and even')
elif a>0 and a%2!=0:
    print('a is pos and odd')
elif a==0:
    print('a is xero')
else:
    print('a is neg')


#or
user = 'James'
access_level = 8
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')
