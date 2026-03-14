# Writing Data in a file.
#
# There are two methods to write data in file
# 1) write()
# 2) writeLine()

fileOpen = open("writeDemo.txt",'w')
fileOpen.write("Itter pitter cheater")
fileOpen.write("How are you doing")
fileOpen.close()