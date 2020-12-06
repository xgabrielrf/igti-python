import numpy as np

## Não esquecer de instalar o numpy:
#pip install numpy==1.19.3
#OBS: É necessário instalar a versão 1.19.3. Existe um bug no windows com a versão 1.19.4

#help(np.array)

print('Valores originais: ')
x = np.array([[1.,1.],[1.,1.]])
y = np.array([[1.,0.],[0.,1.]])
print(f'x: \n{x}')
print(f'y: \n{y}')

print('\nMultiplicação padrão: ')
print(f'Multiplicação entre dois arrays: \n{x * y}')
print(f'Multiplicação com float/int: \n{x * 2}') #Broadcasting

print('\nMultiplicação padrão + ones: ')
print(f'Criando matriz com valores 6: \n{6 * np.ones((10,3))}')


print('\nMultiplicação matricial: ')
print(f'Multiplicação matricial (np.dot): \n{np.dot(x,y)}')
print(f'Multiplicação matricial (@): \n{x @ y}')
print(f'Multiplicação matricial (.dot): \n{x.dot(y)}')
