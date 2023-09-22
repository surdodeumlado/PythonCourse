# Decoradores são "syntax sugar"
# simplifica o uso das funções decoradoras sem que tenhamos que escrever 300 coisas

def createFunction(function):

    def inner(*args, **kwargs):

        for arg in args:
            isString(arg)

        return function(*args, **kwargs)

    return inner


# a função inverte string agora virará a função inner de dentro da createFunction
@createFunction
def inverte_string(string):
    return string[::-1]


def isString(parameter):
    if not isinstance(parameter, str):
        raise TypeError('Parameter need to be a str')


bom_dia = inverte_string('Olá, bom dia!!!')


print(bom_dia)
