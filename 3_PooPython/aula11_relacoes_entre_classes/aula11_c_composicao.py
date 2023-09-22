# Relações entre classes: associação, agregação e composição

# Composição é uma especialização da agregação.

# Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
        # com isso daqui, estamos instanciando endereço dentro de cliente, e quando cliente deixar de existir, o endereço também passa a deixar de existir

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Daniel')

cliente1.inserir_endereco('rua tal do tal', 999)
cliente1.inserir_endereco('rua lero lero', 765)

# a rua farinhada só sumirá depois das outras pq ela NÃO está atrelada à alguma classe pai
endereco_externo = Endereco('rua farinhada', 1999)

cliente1.listar_enderecos()

del cliente1  # APAGUEI O CLIENTE, GARBAGE COLLECTOR PEGOU O RESTO


# GARBAGE COLLECTOR
print('#####################\nAQUI TERMINA O CÓDIGO\n#####################')
# SE NÃO APAGARMOS A CLASSE DE CLIENTE, O GARBAGE COLLECTOR SERÁ RESPONSÁVEL POR DESALOCAR AS CLASSES DA MEMÓRIA AO FINAL DO PROGRAMA, MAS SE APAGARMOS A CLASSE PAI ANTES DO CÓDIGO ACABAR, O GARBAGE COLLECTOR FARÁ O SERVIÇO ANTES DO CÓDIGO ACABAR
