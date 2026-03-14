import os

files = []
merged_data=""

while True:
    f_name = input("Enter the file name: ")
    files.append(f_name)
    ans = input("Want to add another file?(y/n)").lower()
    if ans!='y':
        break



for file in files:
    filename = file + '.txt'
    if os.path.isfile(filename):
        f = open(filename,'r')
        merged_data = merged_data + f.read()+'\n'
        f.close()
print(merged_data)

with open(input("Enter your file name : ")+'.txt',mode='w',encoding='utf-8') as f:
    f.write(merged_data)
    print("merging is done, thanks!!")