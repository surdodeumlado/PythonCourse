# Tudo que usamos em list comprehension cabe aqui também !

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

for chave, itens in produto.items():
    print(chave, itens)

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor
    in produto.items()
    if chave != 'categoria'  # filtro
}

lista = [
    {'a', 'valor a'},
    {'b', 'valor b'},
    {'c', 'valor c'},
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }

print(dc)
print(dict(lista))

s1 = {i for i in range(10)}

print(s1)
