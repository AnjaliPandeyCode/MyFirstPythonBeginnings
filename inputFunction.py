# input function - take input from the user, when we use input() function, python pause the program and waits for user to type something and press enter.

# a  = input()
# print(a)

# name = input("Enter your name: ")
# print(f"Welcome {name} to the Python classes")

# x = input("Enter first number: ")
# y = input("Enter second number: ")
# print(f" Sum of {x} and {y} is {int(x) + int(y)}")


# Practice Question : Write a program to input student name and marks of 3 subjects. 
# Print name and percentage.

name = input ("Enter student name: ")
marks1 = input ("Enter marks for 1st subject: ")
marks2 = input ("Enter marks for 2nd subject: ")
marks3 = input ("Enter marks for 3rd subject: ")
total_marks = int(marks1) + int(marks2) + int(marks3)
percentage = (total_marks/300) * 100
print(name)
print(f"Percentage is: {percentage}%")
