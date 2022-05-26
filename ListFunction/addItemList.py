
#This will add orange  to the end of the item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print (thislist)
 
#Insert an item to the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "Melon")
print (thislist)

#Extend an item to the second position:
color1 = ["Orange", "Blue", "Red"]
color2 = ["Black", "White", "Purple"]

color1.extend(color2)
print (color1)


#An lements of a tuple can also be added or join to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

