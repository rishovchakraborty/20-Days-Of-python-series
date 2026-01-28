# Regular Expressions

# A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.


# re.match(): searches only in the beginning of the first line  of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string

# syntax
# re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore


import re
text='I love python and It\'s so easy. python is an interpreted lang.'
pattern='python'

match = re.match(pattern,text)
print(match) # "python" is not at index 0, so re.match() fails.

pattern2 = 'I lov'
match = re.match(pattern2,text)
print(match) # <re.Match object; span=(0, 5), match='I lov'>

match=re.search(pattern,text)
print(match) # <re.Match object; span=(7, 13), match='python'>
print(match.span()) # (7, 13)
print(match.span()[0])

