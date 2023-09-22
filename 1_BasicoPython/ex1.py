nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if (bool(nome) == True and bool(idade) == True):
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome possui espaços')
    else:
        print('Seu nome não possui espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Você deixou campos vazios.')
