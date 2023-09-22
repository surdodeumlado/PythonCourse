produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Filtro permite que, com list comprehension, possamos filtra algo

# produtos_acima_de_20 = [p for p in produtos if p['preco'] > 10]
# com list comprehension

# com programação funcional
produtos_acima_de_20 = filter(
    # quero que retorne todos os preços de produtos que seja acima de 10
    lambda p: p['preco'] > 20, produtos
)

# sem lambda
# def filtar_preco(produto):
#     return produto['preco'] > 20


print(*produtos_acima_de_20, sep='\n')
