print('Adicionando novos valores em locais específicos da lista:')
lista = ['Amarelo', 'Verde', 'Branco', 'Preto']
print(lista)
lista.insert(2,'Rosa')
print(lista)

print('\nPegando último valor:')
print(lista[-1])

print('\nRemovendo um ítem específico:')
lista.remove('Branco')
print(lista)

print('\nRemovendo de uma posição específica:')
lista.pop(0)
print(lista)