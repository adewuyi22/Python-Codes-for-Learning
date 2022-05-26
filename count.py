#counting and getting the total number of data in a variable. 
h = "Hello World"
print ("The total number of data in the variable is: ",len(h)) 

#counts and returns the number of words in a given text.
f = open("textfile.txt", "r")
lines=f.read()
words=lines.split()
print("The total number of words in the textfile is: ",len(words))
