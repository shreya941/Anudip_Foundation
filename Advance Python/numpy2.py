import numpy as np
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.diag(c))

#randint is an inbuilt function of the random module in python3.

rand=np.random.randint(2,3)
print(rand)

#reshape functiom

arr=np.array([1,2,3,4,5,6,7,8,9])
arr2=arr.reshape(3,3)
print(arr2)

#we pass-1 in case we donot want to tell rows and columns. we can only specify 1 unknown dimension

arr3=arr.reshape(-1,3)
print(arr3)

np.random.seed(90)
arr=np.random.randint(0,500,30).reshape(6,5)
print(arr)
#slicing operations::::
print(arr[2:,2:])
print(arr[3:5,2:5])
print(arr[:])
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[4:9])
slicing=arr[4:6]
print(slicing)
print(arr)
slicing[:]=0
print(slicing)
print(arr)

#arange function
ar = np.arange(1,15)
print(ar)

print(ar[ar%2!=0])
print(ar[ar%2==0])
ar[ar%2==0]=0
print(ar)

#conditional printing
ar = np.arange(100).reshape(50,2)
print(ar+2)
print(ar*2)
print(ar**2)


#more functions of array
np.random.seed(122)
ar=np.random.randint(1,21,9).reshape(3,3)
print(ar)
print(np.sum(ar))
print(np.cumsum(ar))
#1=row 0=col
print(np.sum(ar,axis=1))

print(np.sum(ar,axis=0))

#seed function fixes the random integers that numpy would pick
np.random.seed(122)
mat=np.random.randint(1,21,10)
np.random.shuffle(mat)
print(mat)

#unique
print(np.unique(mat,return_index=True,return_counts=True))
print(np.unique(mat).size)
