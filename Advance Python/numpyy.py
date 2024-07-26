#importing numpy to use it's functions and methods
import numpy as np

#conversion of list to array
l=[1,2,3,4,5]
arr=np.array(l)
print(arr)

#different types of array, 1d,2d and 3d
a=np.array(1)
print("this is 0 d array",a)
b=np.array([1,2,3,4])
print("this is 1 d array",b)
c=np.array([[1,2,3,4],[1,2,3,4]])
print("this is 2 d array",c)
d=np.array([[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]])
print("this is 3 d array",d)

#getting to know the dimensions

print("dimension of a :",a.ndim)
print(d.shape)
#1d array is known asvector
#2d array is known as matrix
#3d array is known as tensor

arr=np.array([1,2,3,4,5,6,7])
sarr=arr[1:5]
print(arr)
print(sarr)
sarr[2]=100
print(arr)
print(sarr)
