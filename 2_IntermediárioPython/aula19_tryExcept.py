# try, except, else, finally

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

try:
    a = 8/0
except (IndexError, TypeError) as error:  # error --> criamos uma variavel que recebe os 2 tipos de erro
    print(f'Erro: {error}')
    print(f'Nome: {error.__class__.__name__}')
except Exception as exceptionn:
    print(exceptionn.__class__.__name__)
    print('erro desconhecido')
else:
    print('Não deu erro')
finally:  # finally é um bloco que sempre será executado no try except
    # Dá pra usar o try junto do finally apenas, sem o except.
    # Mesmo que ocorra um erro, o finally SERÁ EXECUTADO antes de fugir pra excessão
    print('finally')
