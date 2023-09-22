import os

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativa = 0
sair = True
while sair:
    letra_digitalizada = input('Digite uma letra: ')

    if len(letra_digitalizada) > 1:
        print('Por favor, digite apenas uma letra.')
        tentativa += 1
        continue

    if letra_digitalizada in palavra_secreta:
        letras_acertadas += letra_digitalizada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    tentativa += 1
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns! Você descobriu a palavra')
        print(
            f'Palavra Secreta: {palavra_secreta}\nTentativas Realizadas: {tentativa}')
        sair = False

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
"""
codigo tentativa abaixo
"""
# palavra = 'perfume'
# tentativas = 0
# tentando = True

# letras = ''
# for i in palavra:
#     letras += '*'

# novaPalavra = letras
# palavraAntiga = letras

# print(f'Palavra secreta: {letras}')

# while tentando:

#     letra = input('Digite uma letra: ')
#     if len(letra) > 1 or letra in ('0123456789'):
#         print('Entrada inválida.')
#         tentativas += 1
#         continue

#     if letra in palavra:
#         x = 0
#         for i in palavra:

#             if letras[x] in

#             if letra == i:
#                 novaPalavra += palavra[x]
#                 x += 1
#             else:
#                 novaPalavra += '*'
#                 x += 1

#     print(f'Palavra secreta: {novaPalavra}')

# acima foi apenas um código tentativa.
