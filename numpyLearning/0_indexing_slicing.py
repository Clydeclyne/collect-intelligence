'''
Created on 2015-6-16

@author: XXYF18
'''
import numpy as np;
import numpy.random as npr ;

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = npr.randn(7, 4)

print names
print data

print names == 'Bob'

print data[names == 'Bob']

print data[names == 'Bob', 2:]

print data[names == 'Bob', 3]

print names != 'Bob'

print data[-(names == 'Bob')]

mask = (names == 'Bob') | (names == 'Will')

print mask

print data[mask]

data[data < 0] = 0

print data

data[names != 'Joe'] = 7

print data


