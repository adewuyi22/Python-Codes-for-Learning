#To delete a file, you must import the OS module, and run its os.remove() function:

import os

try:
    os.remove("newfile.txt")
    print("\nFile deleted successfully.")
except:
    print("\nFile does not exist!")


#Check if file exists, then delete it:
if os.path.exists("myfile5.txt"):
  os.remove("myfile5.txt")
  print("Another file deleted successfully...")
else:
  print("\nThe file does not exist")

  #To delete an entire folder, use the os.rmdir() method:
  try:
      os.rmdir("myfolder2")
      print("\nFolder deleted successfully")
  except:
      print("\nFolder does not exist...")
