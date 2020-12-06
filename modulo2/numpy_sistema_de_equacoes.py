import numpy as np

'''
Exemplo:
Solução de um sistema de equações:
    1*a + 2*b = 7
    3*a - 2*b = -11
    Solução analítica: (a,b) = (-1,4)

Matricialmente:
    Ax = c, onde:
    - x = [a,b]
    - A = [[1,2],[3,-2]]
    - c = [[7],[-11]]
    Solução numérica: x = inv(A) @ c
'''

#Definição do problema
A = np.array([[1,2],[3,-2]])
c = np.array([[7],[-11]])
print(f'A: \n{A}')
print(f'c: \n{c}')

#Solução: x = A^-1 @ c
x = np.linalg.inv(A) @ c # ou x = np.dot(np.linalg.inv(A),c)
print(f'\n(a,b): \n{x.ravel()}')