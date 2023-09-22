# Métodos de classe são métodos que ao invés de 'self' como primeiro parâmetro, receberá a própria classe

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # classmethod faz com que eu possa chamar minha classe sem passar o self, MAS eu obrigatoriamente tenho que passar algum parâmetro ali (que é a própria classe em si)
    @classmethod
    def metodo_de_classe(cls):
        print('Hey!')

    # Nós usamos o classmethod juntamente com as factories, existem factory function, factory method, etc.
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Pessoa_anônima', idade)


print(Pessoa.ano)

p1 = Pessoa('Daniel', 18)
p2 = Pessoa.criar_com_50_anos('Zé maria')
p3 = Pessoa.criar_sem_nome(22)

# Ambos abaixo são métodos de classe
Pessoa.metodo_de_classe()
Pessoa.ano

print(p2.nome, p2.idade)

print(p3.nome, p3.idade)
