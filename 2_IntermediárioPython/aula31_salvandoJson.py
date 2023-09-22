import json

# Para exportar o nosso código python para um JSON, executamos o código abaixo:

# pessoa = {
#     'nome': 'Daniel',
#     'sobrenome': 'Alexandre',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 1234},
#         {'rua': 'R2', 'numero': 4321}
#     ],
#     'altura': 1.70,
#     'numeros_preferidos': (16, 2, 2005),
#     'dev': True,
#     'nada': None,
# }

# with open('aula31.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa,  # dict que enviaremos pro json
#         arquivo,  # nome do nosso open
#         indent=2  # formatação do json
#     )


# =============================================================================================================
# Para IMPORTAR um json para nosso código python, executamos o código abaixo:

with open('aula31.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

for chave in pessoa:
    print(chave, pessoa[chave])
