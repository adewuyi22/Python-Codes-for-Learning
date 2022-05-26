#The pop() method removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020

}
thisdict.pop("year")
print (thisdict) 

#----------------------------------------------------------------------

#The popitem() method removes the last inserted item 
#(in versions before 3.7, a random item is removed instead):
remdictt = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020

}

remdictt.popitem()
print (remdictt) 

#--------------------------------------------------------------

#The del keyword removes/delete the item with the specified key name
remdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020

}

del remdict["brand"]
print (remdict) 


#The clear() method empties the dictionary:
remdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020
}

remdict.clear()
print (remdict) 



