print('*args:')
def print_nomes(*nomes):
    for nome in nomes:
        print(f'Olá, {nome}')

print_nomes('Gabriel', 'Taciani', 'Lincon')

print('\n**kwargs - Criando dicionário')
def minha_funcao(**kwargs):
    print(str(kwargs))

minha_funcao(a=12,b='abc')