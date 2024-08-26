''' NumPy Arrays (Matrizes) é um pacote de Python que lida com números.
Numpy array is a powerful N-dimensional array object which is in the form
of rows and columns. We can initialize NumPy arrays from nested Python
lists and access it elements.
'''
# Numpy Array unidimensional
import numpy as np
import time
import sys
a = np.array([1, 2, 3])
print(a)
print(a.itemsize)

# Numpy array bidimensional
b = np.array([(1, 2, 3), (4, 5, 6)])
print(b)

c = range(1000)
print(sys.getsizeof(5)*len(c))

d = np.arange(1000)
print(d.size*d.itemsize)

Size = 1000000
 
l1 = range(Size)
l2 = range(Size)
a1 = np.arange(Size)
a2 = np.arange(Size)
 
start= time.time()
result=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)
 
start=time.time()
result= a1 + a2
print((time.time()-start)*1000)