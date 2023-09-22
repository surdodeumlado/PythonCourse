# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class CriarNovaClasse:
    def __init__(self, nome, sobrenome):  # o primeiro parâmetro TEM que ser self
        # o SELF referencia o objeto que está instanciando a classe. No caso das de baixo, classe1 e classe2 são quem o self está referenciando.
        self.nome = nome
        self.sobrenome = sobrenome


classe1 = CriarNovaClasse('Daniel', 18)
print(classe1)  # <__main__.CriarNovaClasse object at 0x0000021239D8ED50>
# __main__ é o módulo em que estamos executando
# CriarNovaClasse é o que estamos instanciando
# o resto é onde a classe está localizada na memória

# classe1.nome = 'Daniel'
# classe1.idade = 18
# classe1.altura = 1.70

# sempre que chamamos de novo, temos uma nova instancia da classe, os objetos são objetos diferentes refenrenciando a mesma classe.

classe2 = CriarNovaClasse('João', 22)
# classe2.nome = 'João'
# classe2.idade = 22
# classe2.altura = 1.87


string = 'Daniel'  # str

print(string.upper())
print(isinstance(string, str))
