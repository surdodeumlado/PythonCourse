# reduce - faz a redução de um iterável em um único valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# exemplo: quero reduzir minha lista pra apenas o maior preço
# exemplo2: quero reduzir minha lista pra o valor total de todos os produtos

# List comprehension
preco = (sum(p['preco'] for p in produtos))
print(preco, end='\n')

# Com reduce

# Sem lambda
# def funcao_reduce(acumulador, produto):
#     return acumulador + produto['preco']

# com lambda
total = reduce(lambda x, y: x + y['preco'],  # função
               produtos,  # iterável que vamos trabalhar com
               0  # acumulador, valor que o total vai iniciar pro reduce fazer equação em cima
               )

print(total)
