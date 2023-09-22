import json


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura


p1 = Pessoa('Daniel', 18, 1.70)

CAMINHO_ARQUIVO = 'exercicio1.json'


def dump():  # ADIANDO EXECUÇÃO DA FUNÇÃO DE DUMP COM A FUNÇÃO DUMP()
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(
            p1.__dict__,  # dict que enviaremos pro json
            arquivo,  # nome do nosso open
            indent=2  # formatação do json
        )


if __name__ == '__main__':  # SE ESTIVERMOS MEXENDO DIRETAMENTE COM ESTA FUNÇÃO, O DUMP SERÁ EXECUTADO
    print('Executando dump.')
    dump()
