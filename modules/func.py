import mymodule

#printing from imported module
mymodule.greeting("Mr John")

#printing the elements of a dictionary from imported module
a = mymodule.person1
print(a)

#Create an alias for mymodule called mx:
import mymodule as mx
a = mx.person1["age"]
print("My age is:",a)


#using the  built in python module
import platform
x = platform.system()
print(x)


#List all the defined names belonging to the platform mo
x = dir(platform)
print(x)

