'''
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation
Python has a built-in package called json, which can be used to work with JSON data.
if you have a JSON string, you can parse it by using the json.loads() method.
'''

import json

#Parse JSON - Convert from JSON to Python
x='{"name":"James", "age":25, "Country":"Nigeria" }'

#parse x:
y=json.loads(x)
print(y["age"])


#Convert from Python to JSON
#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)



#You can convert Python objects of the following types, into JSON strings:
print(json.dumps({"name": "John", "age": 30})) #dictionary
print(json.dumps(["apple", "bananas"])) #list
print(json.dumps(("apple", "bananas"))) #tuple
print(json.dumps("hello")) #string 
print(json.dumps(42)) #int
print(json.dumps(31.76)) #float
print(json.dumps(True)) #True
print(json.dumps(False)) #False
print(json.dumps(None)) #None