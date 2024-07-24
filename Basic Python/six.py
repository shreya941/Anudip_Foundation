#SET
months={"shreya","yashika","best","friends"}
print(months)
months.add("since day 1")
months.update({"very very","close"})
print(months)

#discard do not give error if the key is not present in the set but removegives the error

months.discard("very very")
print(months)
months.discard("ver")
print(months)
#months.remove("ver")
#print(months)

#pop removes any data from set

#string

name="i am python learner"
print(name)
print("name[2:4]",name[2:4])
print("name[5:9]",name[5:9])
print("name[:15]",name[:15])
print("name[2:]",name[2:])
print("name[:]",name[:])
print("name[0:17:3]",name[0:17:3])
print("name[::]",name[::])
print("name[::-1]",name[::-1])

#is operator
x=["a","b"]
y=["a","b"]
z=x
print(x is z)
print(x is y)

#capitalize first letter of string

str="kiwi"
str=str.capitalize()
print(str)

str=str.center(16,"-")
print(str)

# count

str=str.count('i',1)
print(str)

#endswith

stri="hello shreyaa"
stri=stri.endswith("yaa")
print(stri)

#find

strin="aaha tamatar bade mazzedar"
strin=strin.find("bade")
print(strin)
sh='''hello'''
print(sh)

#isalnum

sto="0000jjjj"
sto=sto.isalnum()
print(sto)

#isnumeric
ss="009"
ss=ss.isnumeric()
print(ss)

st="jk"
st=st.upper()
print(st)

#strip removes spaces from string

st="-------------------dhdhhd--------------------"
str4=st.lstrip("-")
str5=st.rstrip("-")
str6=st.strip("-")
print(str4)
print(str5)
print(str6)

#replace

rin="aaha tamatar bade mazzedar"
print(rin)
rin=rin.replace("aaha","waah")
print(rin)

#swapcase

























