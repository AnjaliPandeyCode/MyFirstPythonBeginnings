# value = None
# if value:
#     print("value is true")
# else:
#     print("b")


# Q.1 Write a simple program to determine if a given year is a leap year using user input

# year = int(input("Please enter the year: "))
# if (year % 4 == 0 and year % 100 != 0) or \
#     (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# Q.2 Login Authentication using conditional Statement.
# Assume you have a predefined username and password. 
# Write a program that prompts the user to enter a username and password and checks whether they match. Following cases are: 
# Both username and password are correct. 
# Username is correct but password is incorrect. 
# Username is incorrect.

# predefined_username = 'Anjali'
# predefined_password = '123'

# username = str(input("Enter your username: "))
# password = str(input("Enter your password: "))

# if username == predefined_username:
#     if password == predefined_password:
#         print("Welcome! Login is successful")
#     else:
#         print("Incorrect Password!")
# else:
#         print("Incorrect Username!")


# Q.2 Write a program that takes marks in three subjects as input and prints whether the student is eligible for admission
maths = int(input("Enter mathematics marks: "))
physics = int(input("Enter physics marks: "))
chemistry = int(input("Enter chemistry marks: "))
totalmarks1 = maths + physics + chemistry
totalmarks2 = maths + physics
if (maths >= 65 and physics >= 55 and chemistry >= 50 and totalmarks1 >= 180 ) or (totalmarks2 >= 140):
    print("Student is eligible!")
else:
    print("Student is not eligible!")





