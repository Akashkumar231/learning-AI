import os

value = os.path.isfile("demo.txt")

if value:
    print("File value exist here.")
else:
    print("File doesn't Exist")
    

print("Is file exist. : " , value)