# Dict e vars para atributos de instância.

class Pessoa:

    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Daniel', 18)
# p1.nome = 'EITA MUDEI'

# print(p1.nome)


print(p1.__dict__)
print(vars(p1))

# tanto o thunder dict e o vars mostram pra gente a nossa classe em formato de conjuntos. Podemos então, assim, alterar nossa classe igual alterariamos um conjunto.

p1.__dict__['outra'] = 'coisa'
print(p1.__dict__)
print(vars(p1))

del p1.__dict__['outra']
print(p1.__dict__)

# É bom caso queiramos mandar nossa classe para um JSON ou importar valores pra nossa classe de um JSON

dados = {'nome': 'Maria', 'idade': 28}

p2 = Pessoa(**dados)
print(p2.__dict__)
