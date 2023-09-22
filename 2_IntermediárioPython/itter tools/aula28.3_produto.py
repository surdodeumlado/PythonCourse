# Produto
# Gera um produto cartesiano
# Basicamente gera 1 tupla que relaciona dados entre listas para cada possibilidade possível
from itertools import product


def pprint(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'Daniel', 'Maria', 'João', 'Pedro'
]

camisas = [
    ['Preta', 'Branca'],
    ['p', 'm', 'g', 'gg'],
    ['masculino', 'feminino', 'unisex'],
    ['infantil', 'adultos'],
    ['algodão', 'poliester']
]

pprint(product(*camisas))
