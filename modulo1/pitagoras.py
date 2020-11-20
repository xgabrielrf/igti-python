cateto1 = input('Digite o valor do primeiro cateto: ')
cateto2 = input('Digite o valor do segundo cateto: ')

hipotenusa = ((int(cateto1)**2)+(int(cateto2)**2))**0.5

print(f'A hipotenusa é: {hipotenusa:.2f}')

if cateto1 >= cateto2:
    maior_cateto = cateto1
    menor_cateto = cateto2
else:
    maior_cateto = cateto2
    menor_cateto = cateto1
print('\n                 /|')
print('                / |       ')
print('               /  |       ')
print('       -----> /   |       ')
print('       |     /    |       ')
print(f'       |    /     |  <-- {maior_cateto}   ')
print('       |   /      |')
print('       |  /_______|')
print('       |      ^')
print(f'       |      {menor_cateto}')
print(f'       {hipotenusa:.2f}')
