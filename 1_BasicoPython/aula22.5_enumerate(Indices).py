# Enumera listas
# Ele faz isso: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# cria tuplas dentro da lista com o índice primeiro e depois o valor
lista = [1, 2, 3, 4, 5]

lista.append(6)

# lista_enumerada = enumerate(lista)

# print(next(lista_enumerada))

for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)

lista_enumerada = list(enumerate(lista, start=19))
print(lista_enumerada)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor} ')
