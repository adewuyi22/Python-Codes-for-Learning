#Print all items in ascending order:
thislist = ["Cherry", "Carrot", "Banana", "Apple"]
thislist.sort()
print (thislist)

#Print all items in ascending order:
num = [20, 45, 10, 50, 5, 15]
num.sort()
print(num)

#This will print in Descending order (Reverse)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Print in reverse order for numbers
num = [20, 45, 10, 50, 5, 15]
num.sort(reverse=True)
print(num)

print("\n")

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Printing the sort list in lowercase
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#This will print in reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
