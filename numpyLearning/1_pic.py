'''
Created on 2015-6-17

@author: XXYF18
'''
import numpy as np;
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print ys
z = np.sqrt(xs ** 2 + ys ** 2)
print z
''' line
'''
#plt.plot([1,2,3])
#plt.ylabel('some numbers')
#plt.show()

plt.imshow(z); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()

#plt.imshow(z,cmap=plt.gray); plt.colorbar()
#plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
#plt.show()