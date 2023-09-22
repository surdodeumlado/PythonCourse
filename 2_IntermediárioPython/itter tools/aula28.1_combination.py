# combinação
# Ordem não importa, iterável + tamanho de grupo
# Ordem não importa = Se vier os dados ('Daniel', 'Maria') e os dados ('Maria', 'Daniel'), ambos são os mesmos dados

from itertools import combinations


def pprint(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'Daniel', 'Maria', 'João', 'Pedro'
]

camisas = [
    ['Preta', 'Branca'],
]

pprint((combinations(pessoas, 2)))  # grupo de 2
pprint((combinations(pessoas, 3)))  # grupo de 3
pprint((combinations(pessoas, 4)))  # grupo de 4
