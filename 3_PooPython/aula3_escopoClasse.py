class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        # print(variavel) <----- não consigo fazer isso pq a variavel tá refinida só no init (escopo local)

        # Qualquer método que tiver o self, vai ter acesso no escopo inteiro da classe.
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='leão')
print(leao.nome)
print(leao.executar('maçã'))
