

# In x mode it just not allowed to write in existing file to prevent losing of data .
file1 = open("first" ,mode='x')
file1.write("Hello , how are you")
file1.close()