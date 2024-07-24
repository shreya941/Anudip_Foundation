
for x in range(10,500):
    if(x%7==0 and x%10==0):
        print(x,"divisible by 10 and 7")
count=0
for i in range(100,1000):
    if(i%2==0 and i%3==0):
        count+=1
print("total : ",count)       
i=100
while(i<1000):
    if(i%3==0 and i%2==0):
        print(i, end=" , ")
    i+=1
  
        
