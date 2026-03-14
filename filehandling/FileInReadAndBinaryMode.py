file=open("ReadAndBinary.txt",'w')
if file:
    print("File Opened Successfully.")
    name = input("Enter your name : ")
    designation = input("Enter your designation : ")
    company = input("Enter your organization name : ")
    file.write(name)
    file.write(designation)
    file.write(company)
    file.close()
    print("Closing File")

print("File Closed ? " , file.closed)


# // Reading in Text Mode
file=open("ReadAndBinary.txt",'r')

if file:
    print("File Opened Successfully.")
    content = file.read()
    print(content)
    file.close()

print("File Closed ? " , file.closed)

file=open("ReadAndBinary.txt",'rb')
if file:
    print("File Opened Successfully.")
    content = file.read()
    print(content)
    file.close()

print("File Closed ? " , file.closed)