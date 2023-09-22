# Podemos usar, por exemplo, para validar se o usuário tá mandando um caractere repetido ou não
letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    print(letras)

    if letra == 'i':
        print('Parabéns, encontrou a letra misteriosa')
        break
