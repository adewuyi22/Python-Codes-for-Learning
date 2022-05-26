#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    xy = "Executed successfully..."
    print(x) #This statement will raise an error, because x is not defined:
except:
    print("An error occured")


'''
You can define as many exception blocks as you want, 
e.g. if you want to execute a special block of code for a special kind of error:
Print one message if the try block raises a NameError and another for other errors:
'''
try:
  print(y)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


'''
You can use the else keyword to define a 
block of code to be executed if no errors were raised:
'''

try:
  print("\nHello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")  
finally:
    print("The 'try except' is finally finished\n")


#Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")



#Raise a TypeError if x is not an integer:
yy = "hello"
if not type(yy) is int:
    raise TypeError("Only integers are allowed")