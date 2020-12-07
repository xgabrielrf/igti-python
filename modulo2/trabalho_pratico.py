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

'''
#Código 7
X = np.array([[1, 3], [11, 10]])
print(np.mean(X[X > np.pi]))
'''

'''
#Código 8
data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no'] 
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


#Código 9
df = pd.DataFrame(data=data, index=labels)

print(df)
'''