# operators - operators are symbol that performs operations on variables and values

# 1. Arithmetic Operator
# a = 5
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)


# 2. Comparison Operator - output is boolean value (true or false)
# a = 5
# b = 3
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)


# 3. Assignment Operator ' = '
# a = 5 


# 4. Logical Operator 
# Rules for AND operator:    # Rules for OR operator:
# True + True = True         # True + False = True
# False + True = False
# False + False = False
# a = 5 
# b = 10
# print(a>10 and b<10)
# print(a==5 or b<15)


# 5. Identity Operator - is, is not
# x = [1,2,3] # this is a list
# y = x
# z = [1,2,3]
# print(x is y)  # is operator
# print(x is z)  # is operator
# print(x is not z)  # is not operator

# 6. Membership operators - in, not in
my_list = ['apple', 'orange', 'banana']
print('apple' in my_list)  #apple is in the list so result is true

# 7. Bitwise operator - AND &, OR |, XOR ^, NOT ~ etc // we use symbol
a = 5        # 5 in binary - 0101
b = 3        # 3 in binary - 0011
print(a | b) # 1 in binary - 0111
