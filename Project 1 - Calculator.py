# Q.1 - Write a Python program to create a calculator that can perform at least five different mathematical operations, such as
# addition, subtraction, multiplication, division, and average, ensure that the program is user-friendly, prompting for input 
# and displaying the results clearly.

# STEP -1 CREATING FUNCTION
def addition(num1, num2):   # parameters are num1, num2
    return num1 + num2
   
def subtraction(num1, num2):   # parameters are num1, num2
    return num1 - num2

def multiplication(num1, num2):   # parameters are num1, num2
    return num1 * num2

def average(num1, num2):   # parameters are num1, num2
    return (num1 + num2)/2

def divide(num1, num2):   # parameters are num1, num2
    return num1 / num2

# STEP -2 USER INPUT
print("Please select a operation:\n"\
    "1. Addition\n" \
    "2. Subtraction\n"\
    "3. Multiplication\n" \
    "4. Average\n" \
    "5. Division\n")

select_operation = int(input("Select any operation from 1,2,3,4,5: "))

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# STEP -3 PRINT THE RESULT
if select_operation == 1:
    print("The sum of two numbers are: ", addition(num1, num2))

elif select_operation == 2:
    print("The subtraction of two numbers are: ", subtraction(num1, num2))

elif select_operation == 3:
    print("The multiplication of two numbers are: ", multiplication(num1, num2))

elif select_operation == 4:
    print("The average of two numbers are: ", average(num1, num2))

elif select_operation == 5:
    print("The division of two numbers are: ", divide(num1, num2))

else:
    print("Invalid operation!!! Please select again.")



