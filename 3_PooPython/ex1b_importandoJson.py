from ex1a_salvandoJson import CAMINHO_ARQUIVO, Pessoa

import json

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

p1 = Pessoa(**pessoa)
print(p1.nome)
print(p1.idade)
print(p1.altura)
