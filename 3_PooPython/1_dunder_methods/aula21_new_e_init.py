# __new__ e __init__ em classes Python __new__ é o método responsável por criar e retornar o novo objeto. Por isso, new recebe cls.

# __new__ ❗️DEVE retornar o novo objeto❗️

# __init__ é o método responsável por inicializar a instância. Por isso, init recebe self.

# __init__ ❗️NÃO DEVE retornar nada (None)❗️object é a super classe de uma classe


class A(object):

    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instancia')
        # o new não recebe self pois vai ser ele quem vai CRIAR o self.
        instancia = super().__new__(cls)
        print('Depois')
        return instancia

    def __init__(self) -> None:
        print('Sou o init')

    def __repr__(self) -> str:
        return 'A()'


# por baixo dos panos, o python tá fazendo isso:
# a = object.__new__(A)
# a.__init__()
a = A()
