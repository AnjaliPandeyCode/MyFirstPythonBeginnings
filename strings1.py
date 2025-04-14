# Strings in Python - sequence of characters.
  # strings are closed within single '', double "", or triple ''' quotation marks.


# Formatted String - way to insert variables or expressions inside a string
# Types of formatted strings:
# 1. Old-style formatting(% operator)
# 2. str.format() method
# 3. F-strings(formatted string literals) - most convinient

# 1. Old-style formatting(% operator)
# name = "Anjali"
# age = 25
# print("My name is %s and I'm %d years old"%(name,age))   # %s and %d are placeholers for string and int

# 2. str.format() method - more powerful and flexible than the old-style % formating
# name = "Anjali"
# age = 25
# print("My name is {} and I'm {} years old.".format(name,age))

# name = "Anjali"
# age = 25
# print("My name is {1} and I'm {0} years old.".format(name,age)) # indexing starts from 0, so name position is 0 and age = 1.

# print("My name is {name} and I'm {age} years old.".format(name = 'Anjali',age = 25)) # advantage = we can give variable and value in same line.

#3. F-strings(formatted string literals) - most convinient and more powerful
# name = "Anjali"
# age = 25
# print(f"My name is {name} and I'm {age} years old.")
# print(f"After 5 years I'll be {age + 5} years old.")


# ESCAPE characters - special characters used in strings to represent whitespace, symbols or control characters
# Escape character is a "backlash \" \n - new line and \t -for tab(space)

# print("Hello\nWorld")
# print("Hello\tWorld")

# String Operators:
# 1. ' + ' : Concatenation - adds two or more strings
# 2. ' * ' : Repetition - muliple same String
# 3. '[]'  : Slice - gives the character from the indexing 
# 4. '[:]' : Range Slice - gives the character from the given range
# 5. 'in'  : Membership - returns true if character exists in the given string
# 6. 'not in'  : Membership - returns true if character does not exists in the given string
# 7. 'r/R' : Raw string - supress actual meaning of Escape characters
# 8. ' % ' : Format - performs string formatting


# a = 'Anjali'
# b = 'Pandey'

# print (a + b)
# print (a * 2)

# if 'n' in a :
#         print("Yes")
# else:
#         print("No")

# print (r"Anjali\nPandey")  # -- supressed escape characters, will print all the message

