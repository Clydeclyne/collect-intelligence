'''
Created on 2015-6-16

@author: XXYF18
'''
import numpy as np;

arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print arr
'''
To select out a subset of the rows in a particular order, you can simply pass a list or
ndarray of integers specifying the desired order:
'''
print arr[[4, 3, 0, 6]]
'''
Hopefully this code did what you expected! Using negative indices select rows from
the end:
'''
print arr[[-3, -5, -7]]

# more on reshape in Chapter 12
arr = np.arange(32).reshape((8, 4))
print arr

print arr[[1, 5, 7, 2], [0, 3, 1, 2]]
print arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]

arr = np.arange(15).reshape((3, 5))
print arr
print arr.T

arr = np.random.randn(6, 3)
print np.dot(arr.T, arr)

arr = np.arange(16).reshape((2, 2, 4))

print arr
arr.transpose((1, 0, 2))
print arr

