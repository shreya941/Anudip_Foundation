import numpy as np
#transpose of array
arra=np.array([[1,2],[2,3],[5,7]])
arr=np.transpose(arra)
print(arr)

#mean of array

arr=np.array([1,2,3,4,5])
print(np.mean(arr))

#argmax() argmin() returns the index of max and min value

print(np.argmax(arr))
print(np.argmin(arr))

#searchsorted() returnss the index where the number should be inserted in a sorted array

arr1=np.array([1,2,3,4,6])
print("index is : ",np.searchsorted(arr1,5))

#extract()

print("elements greater than 3 :",np.extract(arr1>3,arr))


