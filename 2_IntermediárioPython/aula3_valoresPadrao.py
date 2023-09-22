"""
Valores padrão para parâmetros
Ao definir uma função, parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado

refatorar: editar o seu código.
"""


def soma(x, y, z=None):
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)


soma(1, 2, 3)
soma(1, 2)

# Sempre que setarmos padrões nomeados, todos os argumentos seguintes deverão ter valores também


def soma2(x, y=None, z=None):
    if y and z is not None:
        print(x+y+z)
    else:
        print(x)


soma2(3)
soma2(3, 5, 7)
