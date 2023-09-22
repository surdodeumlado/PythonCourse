# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        print('Chamando,', self.phone)
        return 'isso está aparecendo no terminal pois estou retornando no __call__'


call1 = CallMe('91985200639')

retorno = call1()  # só é possivel através do dunder __call__
print(retorno)
