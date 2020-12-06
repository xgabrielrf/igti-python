import numpy as np

A = np.array([1,2,3])
B = np.array([2,0,2])
s = 3

#Menor que
print('Comparação menor que: ')
print(A < B)
print(A < s)

#Menor ou igual
print('\nComparação menor ou igual: ')
print(A <= B)
print(A <= s)

#Maior que
print('\nComparação maior que: ')
print(A > B)
print(A > s)

#Maior ou igual
print('\nComparação maior ou igual: ')
print(A >= B)
print(A >= s)

#Igualdade
print('\nComparação igualdade: ')
print(A == B)
print(A == s)


#Filtragem
print('\nFiltro com condição: ')
cond = A <= 2
D = A[cond]
print(f'A: {A}')
print(f'Condição: \n{cond}')
print(f'D: {D}')
#Ou...
print('\nFiltro com condição V2: ')
print(f'A filtrado diretamenta nele, \nonde pega apenas valores menores ou iguais a 2: \n{A[A <= 2]}')
print(f'Quantidade de elementos: {len(A[A <= 2])}')
