
'''
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

It is a good practice to alway close your file when your are done with it.
'''

#To open a file from the current directory for reading.
f = open("myfile.txt", "r") #or  f = open("myfile.txt", "rt")
print(f.read())


#If the file is located in a different location, you will have to specify the file path, like this:
print("Printing the path of a file")
fr = open("C:\\PythonProject\\File_Handling\\Myfiles\\myfile.txt")
print(fr.read())


#To Read Only Parts of the File you can also specify how many characters you want to return:
f = open("myfile.txt")
print(f.read(5))
f.close()

#Using Readlines: You can return one line by using the readline() method:
fx = open("myfile1.txt", "r")
print(fx.readline()) 
print(fx.readline()) 
fx.close()

fx = open("myfile.txt", "r")
for x in fx:
    print(x)

