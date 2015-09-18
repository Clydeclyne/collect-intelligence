'''
Created on 2015-6-17

@author: XXYF18
'''
import numpy as np;
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

'''list comprehension doing this might look like:
'''
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print result
'''This has multiple problems. 

First, it will not be very fast for large arrays (because all the work is being done in pure Python). 

Secondly, it will not work with multidimensional arrays. 

With np.where you can write this very concisely:
'''
result = np.where(cond, xarr, yarr)

print result

arr = np.random.randn(4, 4)
print arr
print np.where(arr > 0, 2, -2)
print np.where(arr > 0, 2, arr)