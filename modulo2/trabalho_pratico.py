import numpy as np
import pandas as pd

'''
#Código 1
Z = np.zeros((4,))
print(f'Z: {Z}')
'''

'''
#Código 2
Z = np.zeros((4,))
Z[1] = 1.
print(f'Z: {Z}')
'''

'''
#Código 3
Z = np.zeros((4,))
Z[1:] = 1.
print(f'Z: {Z}')
'''

'''
#Código 4
Z = np.zeros((4,))
Z[:-1] = 1.
print(f'Z: {Z}')
'''

'''
#Código 5
X = np.ones((2,2))
X = X * 2
print(f'X: \n{X}')
'''

'''
#Código 6
X = np.array([[1, 2], [3, 4]])
print(f'X: \n{X}')
Y = X[0,:]
Y[1] = 10
print(f'X: \n{X}')
'''