lista = ['Amarelo', 'Verde', 'Branco', 'Preto']
print('Criando contjunto a partir de uma lista: ')
conjunto = set(lista)
print(conjunto)
print(type(conjunto))
print('Obs: Um conjunto nunca tem valores repetidos')

print('\nTrabalhando com operações:')
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
print(f'Conjunto A: {conjunto_a}  Conjunto B: {conjunto_b}')

print('\nUnião entre conjuntos:')
print(conjunto_a.union(conjunto_b))

print('\nInterseção entre conjuntos:')
print(conjunto_a.intersection(conjunto_b))

print('\nDiferença entre conjuntos:')
print(conjunto_a.difference(conjunto_b))

print('\nDiferença simétrica (ou exclusivo, xor) entre conjuntos:')
print(conjunto_a.symmetric_difference(conjunto_b))