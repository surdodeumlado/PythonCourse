nome = 'Daniel Alexandre'
i = 0
x = ''
while i < len(nome):
    x += nome[i]
    print(x)
    i += 1

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     # aqui ocorre um caso de concatenação, o += entre 2 strings concatena ambas
#     novo_nome += letra + ' '
#     indice += 1

# print(novo_nome)

# problema calculadora

sair = True

while sair:

    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    oper = input('Operação desejada [+, -, /, *]: ')

    numeros_validos = None  # flag
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou Ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'
    if oper not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(oper) > 1:
        print('Digite apenas um operador.')
        continue

    print('O resultado da operação é igual à ', end='')
    if oper == '+':
        print(num1_float + num2_float)
    elif oper == '-':
        print(num1_float - num2_float)
    elif oper == '/':
        print(num1_float / num2_float)
    elif oper == '*':
        print(num1_float * num2_float)
    else:
        print('Não deveria chegar aqui.')

    querSair = str(input('Quer sair ? [s/n]: '))
    if (querSair.lower().startswith('s')):
        sair = False
