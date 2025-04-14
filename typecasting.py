# casting in python

a = 1
print(type(a)) # output: <class 'int'>

b = "1"
print(type(b)) # output: <class 'str'>

c = int(b)
print(type(c)) # output: <class 'int'>
print(a+c)

#name = "Nandini"
#newname = int(name) # here we cannot do typecasting because value is string

# ALL NUMERIC VALUES CAN BE CAST INTO STRING BUT STRING TYPE CANNOT BE CASTED INTO NUMERIC VALUES

#implicit type casting
var1 = 10   #int type
var2 = 15.5 #float type
var3 = var1 + var2
print(var3)
print(type(var3))   

#explicit type casting
int_num = 101
str_num = str(int_num)
print(type(str_num))

a0 = bool (0)
print(a0)
print(type(a0))

a1 = bool (1)
print(a1)
print(type(a1))

