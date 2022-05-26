
#Tuples are immutable list denoted in a normal bracket. 
#In Tuples, you cannot assign any other value to the current values

profession = ('Lawyer', 'Doctor', 'Nurse', 'Engineer', 'Data Analytst', 'Model', 'Journalist')
print (f'My occupation is {profession}')

#Check if "apple" is present in the tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
    print("Apple does not exist.")


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(f" {mytuple}")


fruits = ("tecno", "itel", "iphone")
print(fruits)
