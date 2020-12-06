import numpy as np

x = np.array([[1, 3, 7], [4, 11, 21], [42, 8, 9]])
print(f'x: \n{x}')

print(f'\nTransposição de matriz: \n{x.T}')

print(f'\nTransformações de matriz em vetor: \n{x.reshape(1,9)}')

print(f'\nSoma de todos os elementos: {np.sum(x)}')

print(f'\nSoma ao longo das linhas: {np.sum(x, axis=0)}')

print(f'\nSoma ao longo das colunas: {np.sum(x, axis=1)}')

print(f'\nMédia de todos os elementos: {np.mean(x)}')

print(f'\nMédia ao longo das linhas: {np.mean(x, axis=0)}')

print(f'\nMédia ao longo das colunas: {np.mean(x, axis=1)}')