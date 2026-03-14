# There are three ways of Closing file in Python File Handling.
#
#  1) f.close()
#  2) With try and finally combination
#  3) with statement

with open("demo.txt",'r') as f:
     content = f.read()
     print(content)

