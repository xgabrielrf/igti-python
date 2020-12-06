import numpy as np

## Não esquecer de instalar o numpy:
#pip install numpy==1.19.3
#OBS: É necessário instalar a versão 1.19.3. Existe um bug no windows com a versão 1.19.4

#help(np.array)

print('Array 1D: ')
l = [1,2,3]
x = np.array(l)
print(f'x:\n {x}')
print(f'shape: {x.shape}')

print('\nArray 2D: ')
l = [[1,2,3],[3,4,5]]
x = np.array(l)
print(f'x:\n {x}')
print(f'shape: {x.shape}')

print('\nArray com apenas 0s: ')
dim = (3,3) #shape
x = np.zeros(dim)
print(f'x:\n {x}')
print(f'shape: {x.shape}')

print('\nArray com apenas 1s: ')
dim = (3,3) #shape
x = np.ones(dim)
print(f'x:\n {x}')
print(f'shape: {x.shape}')

print('\nArray com valores dentro de um intervalo, linearmenta espaçados: ')
x_min, x_max = 5,15
x = np.linspace(start=x_min,stop=x_max,num=6)
print(f'x:\n {x}')
print(f'shape: {x.shape}')

print('\nMatriz identidade: ')
n = 4 #4x4
x = np.eye(n)
print(f'x:\n {x}')
print(f'shape: {x.shape}')
'''
print('\nArray aleatória: ')
x = np.random.random(size=(2, 3))
print(f'x:\n {x}')
print(f'shape: {x.shape}')
'''
print('\nCuidados com Slice: ')
x = np.array([1,2,3])
print(f'x antes:\n {x}')
y = x[:2] #Pegando apenas os dois primeiros números de X
y[0] = -1000 #Acaba por alterar tanto em X quanto em Y (compartilha memória)
print(f'x depois:\n {x}')
print('Corrigindo: ')
x = np.array([1,2,3])
print(f'x antes:\n {x}')
y = x[:2].copy() #Assim gera outro objeto na memória
y[0] = -1000
print(f'x depois:\n {x}')