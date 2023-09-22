from functools import partial


def printIter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem)


aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]


def muda_preco_de_produto(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}


novos_produtos = map(muda_preco_de_produto, produtos)

print(*novos_produtos, sep='\n')
print(novos_produtos)  # é um map object
# a diferença de um map object é q ele é um iterator
# Map é basicamente um list comprehension, mas que recebe uma função no primeiro parâmetro e um iterável no segundo parâmetro

# se for mto pequeno da pra fazer com lambda

print(
    list(map(lambda x: x*3, [1, 2, 3, 4]))
)
