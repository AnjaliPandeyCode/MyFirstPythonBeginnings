# Strings in python
# String Methods

# 1. String Indexing - can access individual char. in a str using their index, first char = 0 index & last char = -1 index
# Index - position of the character

# name = 'Anjali P' # blank space is also a character, taking space in the memory
# print(name[3])
# print(name[-2])

# 2. String Slicing - subset of characters from a string using a range
# syntax:  string[start : end : step] // start default value = 0

# name = 'Anjali'
# print(name[0 : 2])

# name = 'AnjaliPandey'
# print(name[-3 :])  # last 3 characters of string

# name = 'AnjaliPandey'
# print(name[:])  # to print all characters of the string, 2 ways of writing ':' or ': :' 

# name = 'AnjaliPandey'
# print(name[ : :-1])  # to reverse the string

# 2. String Methods
# len()    - returns the length of string
# upper()  - convert string into upper case
# lower()  - convert string into lower case
# title()  - convert the 1st character of string into upper case
# strip()  - removes whitespaces- spaces, tab or newline characters 
# count()  - returns the numbers of time value repeated in the string
# find()   - tells the position of value in the string
# split()  - split the string at the specified separator and returns a list
# replace(old,new) - replace old substring with a new substring

word = 'hello, Anjali'
print(len(word))
print(word.upper())
print(word.lower())
print(word.count('l'))
print(word.find('H'))
print(word.split(' '))
print(word.title())
print(word.replace("Anjali", "Nandini"))

word2 = '         hello, Anjali'
print(word2.strip()) # removed spaces

zwords = ("Anjali", "is", "great")
print("-".join(zwords))
