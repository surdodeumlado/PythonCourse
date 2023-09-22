"""
Existem 2 tipos de argumentos
Argumentos nomeados:
  Possuem nome

Argumentos não nomeados (posicionais):
  não possuem nome
"""


def soma(a, b):
    print(f'{a=}, {b=} | {a} + {b} = {a+b}')


# Não nomeados, aqui vai seguir a ordem que passamos os parametros
soma(1, 2)
soma(2, 1)
# Nomeados, aqui a ordem eh tanto faz, os valores vão ser atribuidos às variaveis
soma(a=1, b=2)
soma(b=2, a=1)

# Também podemos misturar argumentos não nomeados com nomeados, porém, quando nós botarmos 1 argumento nomeado, todo o resto também tem que ser nomeado


def soma2(a, b, c):
    print(a + b + c)


soma2(1, c=3, b=2)
