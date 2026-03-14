# Normal Read Function
fileOpen=open("ReadAndBinary.txt",'r')
content = fileOpen.read()
print(content)
fileOpen.close()

#  ReadLine function
fileOpen = open("ReadAndBinary.txt")
content=fileOpen.readline()
print(content)
fileOpen.close()

# ReadLine Function
fileOpen = open("ReadAndBinary.txt")
lines = fileOpen.readlines()
for line in lines:
    print(line,end="")
fileOpen.close()