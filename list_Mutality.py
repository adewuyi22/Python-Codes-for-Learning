#Working with list. List is a Datatype having a particular order of items or elements

colour=['Blue', 'Red','Yellow', 'Green', 'Brown']
print(f'\nMy colour list are {[colour]}')


print(f'\nMy best color is {colour[0]} and {colour[4]}.')

#changing the element of a list. Changing 'Red' to 'White'
colour[1]='White'
print(f'My friend likes {colour[1]} colour.\n')

#Removing data from a list using the 'pop' function
colour.pop(3) #The 'Red Colour' has been removed from the list
#print(f'Modifying Colours {colour}')
print(f'element 3 removed. {colour}')


#Modifying the data from a list using the 'insert' function
colour.insert(3, 'pink') #The 'Green Colour' would be change to pink from the output list
print(f'New pink colour added to element 3 {colour}')

del colour[2]
print(f'\nElement 2 Deleted. {colour}')