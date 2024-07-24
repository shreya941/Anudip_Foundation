#file handling in text files
file=open("new.txt",'w')
file.write("heheheheh")
file.write(" oh no ")
file.close()
file=open("new.txt",'w')
i=file.tell()
print(i)

file.close()
