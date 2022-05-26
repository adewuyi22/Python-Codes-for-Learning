'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
'''

# Append - will add data to the end of the file. 
# If the file does not exist, it will be created automatically. 
fa = open("myfile1.txt", "a")
fa.write("More content added to file\n") 

print("\nData Successfully added...")
fa.close()

#This will overwrite the content of the file.
fw = open("myfile2.txt", "w")
fw.write("This is an overwrite content of the file.")
print("\nFile override successfully...")
fw.close()

#To create a new file without writing to it. But this will throw an error if the file already exist. 
try:
    cf = open("newfile.txt", "x")
    print("\nNew File created successfully...")
except:
    print("\nError, file already exist!")
