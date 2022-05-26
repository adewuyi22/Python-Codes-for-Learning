
#This will remove banana from the list item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print (thislist)
 
#This "Pop" function will remove from a list item according to the specified index number
thislist = ["apple", "orange", "Melon"]
thislist.pop(1)
print (thislist)

#This will only remove from the last index
thislist = ["apple", "orange", "Melon"]
thislist.pop()
print (thislist)

#del keyword can also be use to remove a list item
thislist = ["apple", "orange", "Melon"]
del thislist[0]
#del thislist[0] #This will delete the entire list
print (thislist)

#The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


