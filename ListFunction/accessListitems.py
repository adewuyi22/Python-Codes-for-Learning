thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#Skip the first and second, Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This example returns the items from the beginning to the fourth list, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print(f'Available fruits are {thislist}')



