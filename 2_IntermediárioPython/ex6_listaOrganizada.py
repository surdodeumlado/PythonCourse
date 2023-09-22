import copy
from pprint import pprint

from exercicio6_package import produtos

# https://pythonacademy.com.br/blog/args-e-kwargs-do-python
# Explica o **p

novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1, 2)}
    for p in copy.deepcopy(produtos)
]

produtos_ordenado_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

produtos_ordenado_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

pprint(produtos_ordenado_por_nome)
print()
pprint(produtos_ordenado_por_preco)
