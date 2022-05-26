
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020,

}

x=thisdict["model"]
print(x)

#To add a new item using key
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change

car["color"] = "red"
print(x) #after the change


#Check if "model" is present in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964  
}
if "model" in thisdict:
  print("\nYes, 'model' is one of the keys in the thisdict dictionary")
else:
  print("Model does not exist!")

