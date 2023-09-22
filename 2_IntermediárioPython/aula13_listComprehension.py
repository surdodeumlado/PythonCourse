import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# List comprehension é uma forma rapida de criar listas a partir de iteraveis


lista = []

for numero in range(10):
    lista.append(numero)

print(lista)

# Esta é a maneira sem list comprehension de adicionar coisas dinamicamente em uma lista
# Há como fazer isso com list comprehension

lista = [numero for numero in range(10)]
# ---> Isso é uma lista comprehension
# Fazemos um for dentro da lista e, mais a esquerda, passamos o que queremos adicionar na lista durante o for
# Nesse caso, estamos adicionando os numeros de 0-9
print(lista)

# o list comprehension permite que façamos operações dentro do list também

lista = [
    numero * 2
    for numero in range(1, 11)
]

print(lista)

# Mapeamento ==================================================================================================
# Significa que transformamos uma lista em uma nova lista, talvez transformando os dados, mas SEMPRE mantendo o mesmo tamanho da lista original

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 40, },
    {'nome': 'p3', 'preco': 60, }
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]  # isso aqui já é um mapeamento

print(*novos_produtos, sep='\n')

# Filtro ======================================================================================================
# Filtragem, posso escolher entre incluir ou não tal elemento na lista
# lista = [n for n in range(10) if n < 5]  <----- o if é o filtro

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10 and produto['preco'] >= 20
]

p(lista)

# Lista com mais de um for ====================================================================================

# for x in range(1, 11):
#     for y in range(1, 11):
#         print(x*y, end=' ')
#     print()
# Tabuada de 0 - 10 dos números de 0 - 10, fazendo em list comprehension fica assim:

lista_tabuada = [
    x * y
    for x in range(1, 11)
    for y in range(1, 11)

]

for tabuada in lista_tabuada:
    print(tabuada)
