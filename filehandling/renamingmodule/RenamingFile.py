import os

# D:\Github_Repository\Learning AI\filehandling\renamingmodule\images

path = input("Enter path where images are stored : ")
path = path.replace('\\','/')
print(path)
path = path + '/'
imageList = os.listdir(path)
print(imageList)
print(path)
index = 1
for image in imageList:
    newName = path+"dish"+str(index)+'.jpg'
    old_name = path+image
    os.rename(old_name,newName)
    index=index+1