# Herança simples - Relações entre classes

# Associação - um objeto usa o outro
# Agregação - um objeto possui parte do outro
# Composição - um objeto é dono de um outro
# Herança - É um objeto, herda um objeto

# Herança vs Composição

# Classe principal (Pessoa)
#   -> super class, base class, parent class

#  Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class Foo(object):  # este (object) é herança

class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.__class__.__name__)


class Cliente(Pessoa):  # cliente herda a classe PESSOA, tudo que está dentro de pessoa está disponível em cliente
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Daniel', 'Pinho')
c2 = Aluno('Maria', 'Madalena')

print(c1.nome, c1.sobrenome)
print(c2.nome, c2.sobrenome)

c1.falar_nome_classe()
c2.falar_nome_classe()


# ESTOU CONSEGUINDO USAR TANTO A CLASSE CLIENTE QUANTO CLASSE ALUNO POIS AMBAS ESTÃO HERDANDO ELEMENTOS DA CLASSE PESSOA.
