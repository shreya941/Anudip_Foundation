#explicitly throwing an exception 
print("enter two numbers")

try:
    a = int(input("enter the 1St number"))
    b = int(input("enter the 2nd number"))
    print(a+b)
except ValueError as e:
    print(e)
