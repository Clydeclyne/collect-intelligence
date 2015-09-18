'''
Created on 2015-6-17

@author: XXYF18
'''
import numpy as np;
import random
position = 0
walk = [position]   
steps = 1000
for i in xrange(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

print walk.min()
print walk.max()
print (np.abs(walk) >= 10).argmax()

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print walks
hits30 = (np.abs(walks) >= 30).any(1)
print hits30