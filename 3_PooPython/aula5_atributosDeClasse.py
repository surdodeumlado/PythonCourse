class Pessoa:

    ano_atual = 2022  # <===== atributo da classe
    # este atributo é algo que sera constante e usado em TODAS AS VEZES que instanciarmos esta classe.

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Daniel', 18)
p2 = Pessoa('Pedro', 22)

# assim que instanciamos atributos de classe fora dela
print(Pessoa.ano_atual)

# Pessoa.ano_atual = 1 <----- fazendo isso, alterariamos o valor do ano para a classe, e este seria o novo valor de ano_atual para TODAS AS INSTANCIAS DAS CLASSES.
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

