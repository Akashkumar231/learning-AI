# File object methods :-

  # 1) readable()
  # 2) writeable()

file = open("hello.txt",mode='w',buffering=4,encoding='utf-8')

if file.writable():
    print("File is writable")
else:
    print("File is not writable")

if file.readable():
    print("File is readable")
else:
    print("File is not readable")

print("Closing the file")

file.close()