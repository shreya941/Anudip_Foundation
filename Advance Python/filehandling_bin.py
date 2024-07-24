#file handling in binary files
import pickle
f=open("hehe.txt",'wb')
li=[10,20,40,50]
pickle.dump(li,f)
f.close()
f=open("hehe.txt",'rb')
d=pickle.load(f)
print(d)
f.close()

#wap to crate a binary file "stu.da" and enter student roll no till he wants
fl=open("stu.da","wb")
dict={'name':"shreya","roll":0}
while True:
    dict.roll=int(input ("enter roll no"))    
    dict.name=input ("enter name")    
f.close()
