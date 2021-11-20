
# Taking Input in python

# Use of input()
val = input("Enter some value : ") # Value enetred by user converts into string
print(val)

# Type 
num = input("Enter some number : ")
print(num)

string = input("Enter some string : ")
print(string)

print(type(num))  # both will have type of string class
print(type(string))

# raw_input() -- same works as input()
# Works in python 2.0 as 
# val = raw_input("Enter some value : ") # Value enetred by user converts into string
# print(val)

#Type Casting

#to integer
num = input("Enter some number : ")
print(num)
print(type(num)) 

num= int(num) #--> Type casting 
print(num)
print(type(num)) 

#to float
num = input("Enter some number : ")
print(num)
print(type(num)) 

num= float(num) #--> Type casting 
print(num)
print(type(num))

#to string
num = input("Enter some number : ")
num= int(num)  
print(num)
print(type(num)) 

num=string(num) #--> Type casting
print(num)
print(type(num)) 