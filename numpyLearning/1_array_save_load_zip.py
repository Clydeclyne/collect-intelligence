'''
Created on 2015-6-17

@author: XXYF18
'''
import numpy as np;
arr = np.arange(10)

np.save('some_array', arr)

print np.load('some_array.npy')
 
np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')
print arch['b']

arr = np.loadtxt('array_ex.txt', delimiter=',')
print arr
