"""
Os dicionarios em python são estruturas de dados do tipo par de chave e valor
chaves podem ser consideradas como "indices" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.
o valor pode ser de qualquer tipo, incluindo OUTRO DICIONÁRIO
usamos as chaves - {} - ou a classe dict para criar dicionários.
imutáveis: str, int, float, bool, tuple
mutáveis: dict, list.

"""

pessoa = {
    'nome': 'Daniel',
    'sobrenome': 'Pinho',
    'idade': 18,
    'altura': 1.70,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'tal tal', 'numero': 321}
    ],
}

# # assim também funciona, mas não é tão usado

# pessoa = dict(
#     nome='Daniel',
#     sobrenome='Pinho',
#     idade='18'
# )

for chave in pessoa:
    print(f'{chave=}, {pessoa[chave]=}')

# tem como também deletar chaves

del pessoa['sobrenome']
print()
print(pessoa)  # vai aparecer sem sobrenome

print(pessoa.get('sobrenome'))  # None
