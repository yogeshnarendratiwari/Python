# Taking multiple inputs

# Split method
# can split python string and can be use for multiple inputs

# input().split(separator, maxsplit) --> Syntax

x,y,z = input("Enter the value : ").split() # by default separator is space and maxsplit is -1 i.e., no limit
print(x)
print(y)
print(z)

# x,y = input().split("e",1)
# print(x)
# print(y)
# print(z) --> can't print because splits only one time and stores in two variable only because have only two parts

# List Comprehension

x,y = [int(x) for x in input("Enter the values : ").split()]
print(x)
print(y)