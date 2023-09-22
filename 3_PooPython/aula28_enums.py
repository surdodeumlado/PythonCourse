# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum


class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()  # 1
    DIREITA = enum.auto()  # 2


# Enum <----- OS VALORES SÃO CONSTANTES
Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

# Maneiras de chamar
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)
# ---retorna o nome-----retorna o valor---------


def mover(direcao: Direcoes):  # direcao é do tipo direcoes

    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
# mover('lado')
