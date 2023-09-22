# Permutação
# Ordem aqui importa, iterável + tamanho de grupo
# Ordem aqui importa = Se vier os dados ('Daniel', 'Maria') e os dados ('Maria', 'Daniel'), ambos são retornados na tela, afinal, ambos são dados diferentes.
# Recomendado quando queremos todas as combinações possíveis

from itertools import permutations


def pprint(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'Daniel', 'Maria', 'João', 'Pedro'
]

camisas = [
    ['Preta', 'Branca'],
]

pprint((permutations(pessoas, 2)))  # grupo de 2
pprint((permutations(pessoas, 3)))  # grupo de 3
pprint((permutations(pessoas, 4)))  # grupo de 4
