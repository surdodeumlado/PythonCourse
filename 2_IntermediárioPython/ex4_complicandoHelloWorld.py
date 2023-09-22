from time import sleep

# Esse exercício não é do curso, fiz por desafio próprio

alfabeto = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

acentos = ['', "'", '"', '!', '@', '#', '$', '%', '¨', '&', '*',
           '(', ')', '-', '_', '=', '+', '´', '`', '[', '{', '~', '^', ']', '}', ';', ':', '/', '?', ',', '<', '.', '>',]

palavra = str(input('Digite uma frase: '))
palavra_formada = ''
for letra in palavra:
    indice = 0

    if letra == ' ':

        sleep(0.045)

        palavra_formada += ' '
        print(palavra_formada, end=' \n')
        continue

    if letra.lower() in acentos:

        while letra.lower() != str(acentos[indice]):

            sleep(0.045)

            palavra_formando = palavra_formada + acentos[indice]
            print(palavra_formando, end=' \n')

            indice += 1
            if letra.lower() == str(acentos[indice]):

                sleep(0.045)

                palavra_formada += acentos[indice]
                print(palavra_formada, end=' \n')
                break

    else:

        while letra.lower() != str(alfabeto[indice]):

            sleep(0.045)

            palavra_formando = palavra_formada + alfabeto[indice]
            print(palavra_formando, end=' \n')

            indice += 1
            if letra.lower() == str(alfabeto[indice]):

                sleep(0.045)

                palavra_formada += alfabeto[indice]
                print(palavra_formada, end=' \n')
                break
