a=input("Enter Your Name : ")

print("The name u have entered : " + a)

demoFile = open("demo.txt",'w')

if demoFile:
    print("File Opened Successfully")

demoFile.write(a)

print("Printing attributes of file.")

print("The name of file "  + demoFile.name)

print("The mode of file  " + demoFile.mode)

print("The encoding of file " + demoFile.encoding)

print( demoFile.closed)

demoFile.close()

demoFile = open("demo.txt",'r')

content = demoFile.read()

print(content)

print("Is Closed?", demoFile.closed)

demoFile.close()

print("Is Closed?", demoFile.closed)

