#Exception handling in python
a = int(input("enter the first no."))
b = int(input("enter the second no."))
try:
    print(a/b)
    print("inside the try block")
    open("hell.txt")
except ZeroDivisionError as e:
    print(e)
except FileNotFoundError as d:
#   print(d)
except(ZeroDivisionError,FileNotFoundError):
   print("something went wrong")
except:
    print("something went wrong")
else:
    print ("else block")
finally:
    print("finally block")
print("newwwwwwwwwww")

