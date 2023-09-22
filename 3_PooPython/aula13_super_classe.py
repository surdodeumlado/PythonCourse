# super() é a super classe na sub classe
# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, child class, derived class


# class MinhaString(str):
#     def upper(self):
#         # super()  # retorna temporariamente a super classe para você, podendo assim usar métodos   da super classe aqui dentro
#         print('ANTES DO UPPER')
#         # esse MinhaString,self dentro do super n precisa, pq ele já lê meio q automaticamente
#         retorno = super(MinhaString, self).upper()
#         print('CHAMOU UPPER')
#         return retorno


# pessoa = MinhaString('Daniel')
# print(pessoa)
# print(pessoa.upper())

class A:

    atributo_a = 'valor a'

    def __init__(self, atributo):  # se passarmos o init na classe mãe, que estará sendo herdada por todas as outras classes, somos obrigados a passar um valor de inicialização para as outras classes (pois o init estará sendo repassada para elas)
        self.atributo = atributo

    def metodo(self):
        print('METODO A')


class B(A):

    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('METODO B')


class C(B):

    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        print('burlei o sistema')

    def metodo(self):
        super().metodo()
        # agora, com o super e sem passar parâmetro nenhum, estaremos puxando o método de B além do método de C

        super(B, self).metodo()
        # se quisermos ser muito especificos, ou puxar o método de A ao invés de puxar o método de B, podemos escrever do jeito acima também. Assim, a partir da classe de B, iremos puxar a classe que B está herdando (que no caso é a classe A)
        print('METODO C')

# a classe C possui TODOS os atributos, porém, a classe C só possui 1 método, que é o que irá printar 'C', pois este método está sobreescrevendo todos os outros


c = C('atributo de inicio', 'coisa qualquer')
print(c.atributo)
print(c.outra_coisa)

print(c.atributo_a, c.atributo_b, c.atributo_c)
c.metodo()
