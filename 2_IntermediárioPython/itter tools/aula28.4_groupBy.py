# groupby - agrupando valores (itertools)
from itertools import groupby
from pprint import pprint

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno):
    return aluno['nota']


alunos_copy = sorted(alunos, key=ordena)

# alunos = ['a', 'a', 'a', 'b', 'c', 'a', 'b', 'c', 'c', 'b', 'a']

# sorted ----> organiza a ordem
grupos = groupby(alunos_copy, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
