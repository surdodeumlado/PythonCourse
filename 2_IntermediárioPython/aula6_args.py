"""
args = Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4, 5, 6, 7, 8

print(x, y, resto)


# def soma(*args):
#     args = list(args)  # sem essa type conversion, seria uma tupla
#     for i in args:
#         print(i)


# print(soma(1, 2, 3, 4, 5, 6, 7))


# Usado para passar uma quantidade grande de argumentos não nomeados.
# Args empacota os argumentos dentro de uma tupla
def soma(*args):
    total = 0
    for numero in args:
        print(f'Total {total} + {numero}')
        total += numero
        print('Total =', total)
    return total
# Para desempacotar os argumentos do args, é só chama-lo novamente com o asterístico de novo


print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
