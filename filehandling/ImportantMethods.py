 # Important Methods

 # tell():-
  # This method  is used to find the current position of a file pointer from the beginning of the file

file = open("ReadAndBinary.txt")
cursor = file.tell()
print(cursor)
file.close()

#  Seek Method will just put the pointer where you will mention the index.
file = open("ReadAndBinary.txt")
index = file.seek(4)
print(index)
file.close()