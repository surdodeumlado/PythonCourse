

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decorador 1')

        def aninhado(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res

        return aninhado
    return fabrica_de_funcoes


# quando puxamos a decoradora, a função decoradora é automaticamente executada, MAS a função aninhada só é executada quando passamos parâmetros para soma
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


mulitplica = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x * y)

somaa = soma(3, 5)

print(soma)
