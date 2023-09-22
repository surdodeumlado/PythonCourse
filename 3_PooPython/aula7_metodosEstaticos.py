# @staticmethod (métodos estáticos)
# os métodos estáticos em python são, em 95% das situações, INUTEIS.
# são métodos que estão dentro das classes, mas não possuem acesso ao self e nem ao cls.

# Em resumo, são funções que existem dentro da sua classe.

class Classe:

    @staticmethod
    def funcao_que_esta_dentro_da_classe(*args, **kwargs):
        print('Oi', args, kwargs)


c1 = Classe()

c1.funcao_que_esta_dentro_da_classe(1, 2, 3)
Classe.funcao_que_esta_dentro_da_classe(nomeado=4)
