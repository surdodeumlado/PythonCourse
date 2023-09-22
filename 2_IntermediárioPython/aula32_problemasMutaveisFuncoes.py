""""
problema dos parâmetros mutáveis em funções python
"""

# def adiciona_clientes(nome, lista=[]):
#      lista.append(nome)
#      return lista

# cliente1 = adiciona_clientes('Daniel')
# adiciona_clientes('Maria', cliente1)
# print(cliente1) -----> ['Daniel', 'Maria']

"""
O problema nessa lista acima é que, lista é mutável, sempre que passarmos a primeira lista pro parâmetro lista=[] do adiciona_clientes, ele sempre estará utilizando a PRIMEIRA LISTA que passamos pra ele, ou seja, se quisermos criar um 'cliente2 = adiciona_clientes('joão')', não será criada uma nova lista, a lista q será utilizada sera a cliente 1 com a adição do 'joão' ao final dela
"""
# cliente2 = adiciona_clientes('João')
# print(cliente2) -----> ['Daniel', 'Maria', 'João']

"""
Para contornar o problema, podemos fazer o seguinte:
"""


def adicionar_cliente(nome, lista=None):
    if lista == None:
        lista = []

    lista.append(nome)
    return lista


cliente1 = adicionar_cliente('Daniel')
adicionar_cliente('Maria', cliente1)
cliente1.append('Pedro')
print(cliente1)

cliente2 = adicionar_cliente('Eraclito')
adicionar_cliente('José', cliente2)
cliente2.append('Marcos')
print(cliente2)
