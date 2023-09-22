# funções decoradas e decoradores
# funções decoradoras são funções que decoram outras funções
# decorar -----> adicionar/ remover/ restringir/ alterar
# decoradores são usados para fazer o python usar as funções decoradoras em outras funções

# =============================================================================================================
# =============================================================================================================
def createFunction(function):

    def inner(*args, **kwargs):

        for arg in args:
            isString(arg)

        return function(*args, **kwargs)

    return inner
# Esta é a função decoradora ==================================================================================
# o trabalho dela é receber uma função interna e esta função não será executada, ela será retornada sem execução para que a pessoa que esteja usando essa função decoradora possa executar esta função e só ai executar a função decorada ====================================================================================
# =============================================================================================================


def inverte_string(string):
    return string[::-1]


def isString(parameter):
    if not isinstance(parameter, str):
        raise TypeError('Parameter need to be a str')


bom_dia = inverte_string('Olá, bom dia!!!')


print(bom_dia)
