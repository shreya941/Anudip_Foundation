# ENTER THE TIME IN SECONDS AND CONTERT IT INTO THE HH:MM:SS FORMAT-------------------------------------------
secs=int(input("enter seconds"))
hour=0
mins=0
sec=0
if(secs>0):
    if(secs>=3600):
        hour=int(secs/3600)
        print(hour,"hours")
    if(secs>=60):
        rem=secs-hour*3600
        mins=int(rem/60)
        print(mins,"minutes")
        sec=secs-(hour*3600+mins*60)
    if(secs<60):
        print(secs,"seconds")
    if(sec>0):
        print(sec,"seconds")


        
#CALCULATE THE PROFIT OR LOSS OF A PRODUCT BY INPUTTING THE SELLING PRICE AND COST PRICE-------------------------
cp=float(input("enter cp in rs:"))
sp=float(input("enter sp in rs:"))
if(cp<0):
    print("invalid costprice")
elif(sp<0):
    print("invalid sprice")
else:
    if(sp>cp):
        print("profit is: ",(sp-cp))
    elif(sp<cp):
        print("loss is: ",(cp-sp))
    else:
        print("equal")



#USING FOR LOOP AND RANGE FUNCTION---------------------------------------------------------------------------------
>>> for j in range(1,10,3):
...     print(j)
