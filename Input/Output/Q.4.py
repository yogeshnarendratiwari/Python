# Output Formatting 
# 1.String modulo ---> %
# print("The date is : %d-%d-%d" % (20,11,2021))
# print("The float number is : %f" % (1.10))

# 2.Format method 
# --> {}
# CODE 1

# print('I subscribed to {} and I love to watch the videos of {}'.format('Techsole','Techsole'))
# print('I subscribed to {0} and I love to watch the videos of {1}'.format('Techsole','App dev'))
# print('I subscribed to {1} and I love to watch the videos of {0}'.format('Techsole','App dev')) # -->DEFAULT COUNTING START =0

# print(f"I subscribed to {'Techsole'} and I love to watch the videos of {'App dev'}")

# print('I had subscribed to {0} and i love to watch the videos of {1} and i like the {other}'.format('Techsole','App dev',other='Videos'))

# print("Student marks : {0:2f} and His/Her Roll no. is : {1:2d}".format(55,12))


# print("Student marks : {a:2f} and His/Her Roll no. is : {b:2d}".format(a=55,b=12))

# student = {'Yogesh' : 99 , 'Neha' : 89 , 'Rahul' : 95 , 'Shruti' : 100 }

# print("Yogesh Marks = {0[Yogesh]:d} ".format(student),"Neha Marks = {0[Neha]:d} ".format(student),"Rahul Marks = {0[Rahul]:d}  ".format(student),"Shruti Marks = {0[Shruti]:d}".format(student),sep='\n')

# 2.Format using string method

# text= "I had subscribed to Techsole"

# print(text.center(40))
# print(text.ljust(40))
# print(text.rjust(40))