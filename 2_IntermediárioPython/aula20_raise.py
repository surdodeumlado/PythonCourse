# raise ---> lançamento de exceções (erros)

# print(123)
# raise ValueError('Deu erro')
# print(456)

def erro_divide_por_zero(d):
    if d == 0:
        raise ZeroDivisionError('Não se divide por 0')
    return True


def verifica_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(f'{n} deve ser int ou float',
                        '\n', f'{tipo_n.__name__} enviado.')

    return True


def divide(n, d):
    verifica_int_ou_float(n)
    verifica_int_ou_float(d)
    erro_divide_por_zero(d)
    return n/d


print(divide('8', 10))
