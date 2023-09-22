"""
iteraveis dentro de iteraveis são tipo
lista dentro de listas
tupla dentro de tuplas
listas dentro de tuplas
tuplas dentro de listas
etc
"""

salas = [
    # 0
    ['Daniel', 'Maria', 'Joana'],

    # 1
    ['Elaine'],

    # 2
    ['Daniel', 'Arthur', 'Manu', (0, 10, 20, 30, 40)]
]

print(salas[0][1])  # Maria, índice 1 da lista 0
# isso aqui são as matrizes, arrays bidimensionais

print(salas[2][3][2])  # 20, índice 2 do elemento 3 dentro do array de índice 2

for sala in salas:
    print(f'Sala: {sala}, elementos: ', end='')
    for elemento in sala:
        print(elemento, end=' ')
    print()
