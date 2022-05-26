#Python has two primitive loop commands:

#1. while loops
#2. for loops

#Using while loop
x=1
while x<6: 
    print(F"LOOPING: {x} \n") 
    x+=1


#With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
  print(f'BREAK : {i}')
  if i == 3:
    break
  i += 1


#Using for loop
floop = "banana"
for fl in floop:
    fl=+1
    print(f'forloop : {floop}')


#Using the range() function
for x in range(6): #for x in range(1, 6): #to start from 1
  print(f"looping range: {x}")


#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#Printing the values from an argument. 
def my_function(child3, child2, child1):
  print("\nThe youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#This will Print each adjective for every fruit
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



#With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("\n i is no longer less than 6")

