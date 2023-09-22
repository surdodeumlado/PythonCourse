import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)

# Modos:
# r -------------------> (leitura), w (escrita), x (para criação)
# a -------------------> (escreve ao final), b (binário)
# t -------------------> (modo texto), + (leitura e escrita)
# Context manager -----> with (abre e fecha)

# Diferenças cruciais entre W e A:
# w -----> o W apaga TUDO que já estiver no arquivo de texto e reescreve o que mandarmos
# a -----> o A não apaga NADA do arquivo, ele começa escrevendo do final. Ou seja, se mandarmos escrever tudo que JÁ escrevemos no aula30.txt, ao invés de "nada acontecer" como aconteceria no W (que na verdade, ele está apagando e escrevendo de novo), o A reescreveria tudo pelo final do arquivo

# Métodos úteis
# write, read -----> (escrever e ler)
# writelines ------> (escrever várias linhas)
# seek ------------> (move o cursor)
# readline --------> (ler linha)
# readlines -------> (ler linhas)

# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink -----> apaga o arquivo (podemos usar qqr uma, tanto faz mesmo)
# os.rename ---------------> troca o nome ou move o arquivo

# Vamos falar mais sobre o módulo json, mas:
# json.dump ------------> Gera um arquivo json
# json.load ------------> Carrega um aquivo json

# Se não especificamos o caminho, ele abre/cria o arquivo na pasta que está o projeto
# Tambem podemos passar um caminho específico
caminho_arquivo = '\\Users\\danie\\OneDrive\\Área de Trabalho\\PythonCourse\\aula30.txt'
# No windows, se usa \\ ao invés de só 1 barra \ pq o \ é utilizado como caractere de escape.
# Se não der certo dessa maneira, podemos usar um r antes das ''
# caminho_arquivo = r'\\Users\\danie\\OneDrive\\Área de Trabalho\\PythonCourse\\aula30.txt'

caminho = 'aula30.txt'

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:

    print(type(arquivo))
    print()

    arquivo.write('Olá mundo!\n')
    arquivo.write('"olá mundo"\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    print()
    arquivo.seek(0, 0)  # Move o cursor de dentro do aula30.txt
    # no caso do seek acima, move o cursor pro inicio do txt de novo
    # este arquivo só é READABLE pq ele é do tipo w+ (writable +)

    arquivo.seek(0, 0)
    # o readline vai ler linha por linha, é tipo um __next__
    # O print já quebra a linha, ent teriamos que tirar a quebra de linha do print pra não conflitar com a quebra de linha do nosso arquivo.write('...\n')

    # Todas estas maneiras ignoram a quebra de linha do print
    print(arquivo.readline(), end='')
    # Todas estas maneiras ignoram a quebra de linha do print
    print(arquivo.readline().strip())
    # Todas estas maneiras ignoram a quebra de linha do print
    print(arquivo.readline().strip())
    # Todas estas maneiras ignoram a quebra de linha do print
    print(arquivo.readline().strip())
    print()

    # READLINES ===============================================================================================
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():  # readlines é uma lista de linhas
        print(linha.strip(), '<----- usando read lines')
    print()
# Sempre que abrirmos um arquivo, devemos FECHAR ele pra não gerar problema
# O 'with open' já abre e fecha automaticamente o arquivo, então não precisamos nos preocupar, MAS caso precisemos fechar o arquivo manualmente usamos o arquivo.close()

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())

# Para apagar o arquivo acima, se utiliza um dos 2 módulos abaixo:

os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo) # é o mesmo que o de cima, funciona igualzin
