def parametro_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)

            final = f'{res} {nome}'

            return final

        return sua_nova_funcao
    return decorador


# a ordem é de baixo pra cima

@parametro_decorador(nome='5')
@parametro_decorador(nome='4')
@parametro_decorador(nome='3')
@parametro_decorador(nome='2')
@parametro_decorador(nome='1')
def soma(x, y):
    return x + y
