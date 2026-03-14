# Demo for the copying content from one file to another file
f1 = open("first",mode='r',encoding='utf-8')
f2 = open("second",mode='w',encoding='utf-8')

lines = f1.readlines()

for line in lines:
    f2.write(line)

f2.close()
f1.close()