from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo  # pausa para o arquivo ser executado
    except Exception as e:
        print('Ocorreu erro')
    finally:
        print('fechando arquivo')
        arquivo.close()


with my_open('aula22_5.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
