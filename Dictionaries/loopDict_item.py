#Print all key names in the dictionary, one by one
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020

}

for x in thisdict:
  print(x) #or print(thisdict[x])

#-----------------------------------------
#You can also use the values() method to return values of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020

}
for x in thisdict.values():
  print(x) #or print(thisdict[x])

#Loop through both keys and values, by using the items() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020

}
for x, y in thisdict.items():
  print(x,y) #or print(thisdict[x])
