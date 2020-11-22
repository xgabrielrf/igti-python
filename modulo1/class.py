print(''''Erro' ao absorver informação de uma variável que foi obtida por classe.
Nesse caso abaixo nós fazemos o carro_2 = carro_1, porém, ao modificar o carro_2,
o carro_1 é alterado indevidamente.

Isso ocorre por conta de quando colocamos carro_2 = carro_1, fazemos o apontamento
para o mesmo objeto na memória. Assim, ao alterarmos um deles, o outro acaba
enxergando o mesmo objeto, com o valor alterado.

Segue o exemplo:''')

class Carro:
    def __init__(self, numero_portas, preco):
        self.numero_portas = numero_portas
        self.preco = preco
        print('Objeto carro instanciado!')
    
    def get_numero_portas(self):
        return self.numero_portas
    
    def set_numero_portas(self, novo_numero_portas):
        self.numero_portas = novo_numero_portas

carro_1 = Carro(4,80000)
print(f'Numero de portas do carro_1 é {carro_1.get_numero_portas()}.')

carro_2 = carro_1

print(f'Numero de portas do carro_2 é {carro_2.get_numero_portas()}.')

carro_2.set_numero_portas(2)
print('erro:')
print(f'Numero de portas do carro_1 é {carro_1.get_numero_portas()}.')
print('alterado:')
print(f'Numero de portas do carro_2 é {carro_2.get_numero_portas()}.')

