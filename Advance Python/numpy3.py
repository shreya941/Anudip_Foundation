import numpy as np
arr=np.array([1,2,3,4,5,8])
#it will convert list to 3 arrays
arr=np.split(arr,3)
for i in arr:
    print(i)
#sorting array in ascending and descending order

#ascending sorting
arr2=np.array([3,2,1,6,7,1,9,0])
arr3=np.sort(arr2)
print(arr3)

#descending sorting
arr4=np.sort(arr2)[::-1]
print(arr4)

#sorting matrix

mat=np.array([[1,2,3],[4,5,6],[0,0,0]])
arr5=np.sort(mat,axis=0)
print(arr5)

#concatenate array
arra=np.array([[1,2],[3,4]])
arra2=np.array([[2,7],[3,3]])

arr_concatenatex=np.concatenate((arra,arra2),axis=1)
arr_concatenatey=np.concatenate((arra,arra2),axis=0)
print(arr_concatenatex)
print(arr_concatenatey)

#vstack and hstack--> same as concateate

arra=np.array([[1,2],[3,4]])
arra2=np.array([[2,7],[3,3]])

arr_concatenatex=np.vstack((arra,arra2))
arr_concatenatey=np.hstack((arra,arra2))
print(arr_concatenatex)
print(arr_concatenatey)

#standard deviation and variance and mean

arra=np.array([1,2,3,4,5])
mean_a=np.mean(arra)
print(mean_a)
std_a=np.std(arra)
print(std_a)
var_a=np.var(arra)
print(var_a)

#percentile
tot=([33,45,66,12,66,78,55,99,12,34,45,55,67,65,76,87,33,55,89,43,54,6524,47])
#50 is the 50th person
percentile_a=np.percentile(tot,50)
print(percentile_a)
