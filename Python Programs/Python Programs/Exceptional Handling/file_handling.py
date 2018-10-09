
f = open("student.text",'w+')
f.write("It's good to study file handling in Python")

f = open("student.text",'r+')
a=f.read()

print a
f.close()  #to close a file
