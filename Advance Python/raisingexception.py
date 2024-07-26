#raising an exception -- used to forcefully raise exception
def fun(age):
    if age>18:
        print("you ca vote")
    else:
        raise ValueError("wait some year");#raising an exception

try:
    fun(13)
except ValueError as e:
    print(e)
    
    

