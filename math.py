#Python has a set of built-in math functions, including an extensive math module, 
# that allows you to perform mathematical tasks on numbers.

#Built-in Math Functions
#The min() and max() functions can be used to find the lowest or highest value in an iterable:


x = min(1, 2, 3, 4, 5)
y = max(5, 15, 10, 8, 9)

print("The minimum number in x is:",x) 
print("The maximum number in is:",y)


#Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x = pow(4, 3) 
print(x)


'''When you have imported the math module, you can start using methods and constants of the module.
The math.sqrt() method for example, returns the square root of a number:'''

import math

x = math.sqrt(64)
print(x)


'''
The math.ceil() method rounds a number upwards to its nearest integer, 
and the math.floor() method rounds a number downwards to its nearest integer, 
and returns the result:
'''
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


#using maths pi
x = math.pi
print("Maths pi: ",x)
