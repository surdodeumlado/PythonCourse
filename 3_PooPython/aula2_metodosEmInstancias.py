class Carro:
    def __init__(self, nome):
        self.nome = nome  # esse self seria o nome do objeto que tá instanciando a classe

    def acelerar(self):  # usamos o self quando queremos que cada classe tenha sua ''função individual''
        print(f'{self.nome} está acelerando')


# nesse caso aqui, o 'fusca' que tá instanciando a classe Carro() é o SELF da classe.
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
# assim também funciona do mesmo jeito q eu na linha de cima
Carro.acelerar(fusca)

celta = Carro('celta')
print(celta.nome)
celta.acelerar()
# assim também funciona do mesmo jeito q eu na linha de cima
Carro.acelerar(celta)

# P.S.: O self na classe NÃO PRECISA SER ESCRITO 'SELF', ele pode ter qualquer nome, a questão é que: TODO PRIMEIRO ARGUMENTO PASSADO EM UMA CLASSE SERÁ CONSIDERADO COMO SELF

# Exemplo:
# class Teste:
#     def __init__(blablabla, nome):
#         blablabla.nome = nome     <------------- o blablabla está fazendo o papel do self
