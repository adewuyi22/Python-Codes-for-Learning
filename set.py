#Sets are written with curly brackets
thisset = {"apple", "banana", "cherry"}
print(thisset)


#Using the set() constructor to make a set:
color = set(("blue", "white", "yellow")) # note the double round-brackets
print(color)

#Accesing the set through Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
if "apple" in thisset:
    print("Apple is present")
else:
    print("Apple is nor present")
#print("banana" in thisset)


#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("Carrot")
print(thisset)



#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("apple") 
print(thisset)
