#Q.1 Write a Python program to input student name and marks of three subjects. Print name and percentage in output

student_name = input("Enter student name: ")
english = input("Enter english marks: ")
physics = input("Enter physics marks: ")
computer = input("Enter computer marks: ")
total = int(english) + int(physics) + int(computer)
percentage = (total/300) * 100
print(student_name)
print(f"Your total percentage is: {percentage}% ")

#Q.2 Write a Python program that collects multiple types of data example name, age, height and student status from user input, stores them in a dictionary and prints out the collected data
# intializing a dictionary
user_data = {}

# input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['status'] = input("Are you a student (yes/no)")

# print the input from user
print(user_data)