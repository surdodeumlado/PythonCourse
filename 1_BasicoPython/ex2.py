# Exercício 1, par ou impar

num = input('Digite um numero inteiro: ')

if num.isdigit():
    entrada_int = int(num)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Impar'

    if par_impar:
        par_impar_texto = 'Par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
# Exercício 2, Horas

horas = input('Que horas são ?: ')
horasInt = int(horas)

if horasInt >= 0 and horasInt <= 11:
    print('Bom dia.')
elif horasInt >= 12 and horasInt <= 17:
    print('Boa tarde.')
else:
    print('Boa noite.')

# Exercício 3, Length nome

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
