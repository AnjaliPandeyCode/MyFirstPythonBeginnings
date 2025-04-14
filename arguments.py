# Arguemts in Functions

# 1. Required Arguments
# def greetings(name):          # one parameter 
#     print(" Welcome to the python course by", name, "!")
   
# greetings("Anjali")           # one value


# 2. Default Arguments
# def greetings(name = "World"):    # World is a default value
#     print("Hello", name)

# greetings()
# greetings("Anjali")

# 3. Keyword Arguments (named argument)- specify arguments by the parameter name
# def divide(a,b):
#     return a/b

# result = divide(100,20)  # positional arguments
# print(result)

# 4. Arbitrary Positional Arguments (*args) -- when unsure how many values(arguments) will pass to function, use *args

# def add_numbers(*args):
#     return sum(args)

# result = add_numbers(1,2,3,4)  # can pass any number of arguments and stores argument as TUPLE
# print(result)

# def greetings2(*names):
#     for name in names: 
#         print(f"Hello, {name}!")
# greetings2("Anjali", 'Nandini', 'Rupali') # passing as a tuple

 # 4. Arbitrary Keywords Arguments (**kwargs) -- key : value (stores arguments as dictionary)

# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}!")
# print_details(name = 'Anjali', age = 25, city = 'Singapore')