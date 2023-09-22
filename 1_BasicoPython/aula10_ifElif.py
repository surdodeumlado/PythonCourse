inp = input('Deseja "entrar" ou "sair" ? ')

if inp == 'entrar':
    print('BEM VINDO MORENO')
elif inp == 'sair':
    print('saida')
else:
    print('Você não digitou entrar nem sair.')

###########################

condicao = True

# Existem IF's soziho, porém não podemos ter nem else nem elif sozinhos no codigo.

if condicao == True:
    print('Código do if.')
else:
    print('Codigo do else.')

primeiroValor = input('Digite um valor: ')
segundoValor = input('Digite outro valor: ')

if primeiroValor > segundoValor:
    print(
        f'O primeiro valor = {primeiroValor} é MAIOR que o segundo valor = {segundoValor}')
else:
    print(
        f'O segundo valor = {segundoValor} é MAIOR que o primeiro valor = {primeiroValor}')
