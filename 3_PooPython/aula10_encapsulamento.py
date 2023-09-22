# Encapsulamento (modificadores de acesso: public, private, protected)

# python NÃO TEM modificadores de acesso, apenas convenções de nomes

# Convenções:

# Sem underline (PUBLIC):
#     pode ser usada em qualquer lugar

# Uma underline _ (PROTECTED):
#     Não deve ser usado fora da classe ou suas subclasses

# Duas underlines __ (PRIVATE):
#     "Name mangling" (desfiguração de nomes) em python
#     só deve usar na CLASSE que foi declarada.

class Foo:
    def __init__(self):
        self.public = 'Isto é publico'
        self._protected = 'Isto é protected'
        self.__private = 'Isto é private'

    def metodo_publico(self):
        print(self.__private,
              'e consigo instanciar isso aqui pq tá dentro da classe que ele foi instanciado')
        self.__metodo_private()
        print('Consegui instanciar o metodo private acima pois estou fazendo isso dentro de um método de dentro da classe que ele foi instanciado.')
        print('Isto é um método publico.')

    def _metodo_protected(self):
        print('Isto é um método protected.')

    def __metodo_private(self):
        print('Isto é um método private.')


cl = Foo()
print(cl.public)
cl.metodo_publico()
