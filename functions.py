# Functions - block of code that performs a specific task
# Benefits - readability and reusable - saves you from writing the same code multiple times

# Function without parenthesis
# def greetings():          # creating function
    # print("Welcome to the python course by Anjali!")
   
# greetings()               # calling function (use function)


# Function with parenthesis
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# def add2nums(num1, num2, num3):   # parameters are num1, num2, num3
#     add = num1 + num2 + num3
#     print("The sum of three numbers are: ", add)

# add2nums(num1,num2,num3)

# Function with return statement
# def add2num(a,b):
#     return a + b
# sum = add2num(1,2)
# print("Total sum is: ", sum)


# Example - function to convert celsius to farenheit using return statement

# def c_to_f(c):
#     f = (c * 9/5) +32
#     return f

# c_to_f(25)  # calling function
# print(c_to_f(25))
# print("With return: ", type(c_to_f))

# Example - function to convert celsius to farenheit using without return statement

# def c_to_f(c):
#     f = (c * 9/5) + 32
#     print(f)
   
# temp = c_to_f(25)  # calling function
# print("Without return: ", type(temp))  # cannot use value further


# Pass statement -- placeholder, do nothing here but write code in future later

def myfuction():
    pass
print("Thank you for learning!")





