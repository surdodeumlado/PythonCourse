"""
Métodos úteis pra serem usados no Dict

len ---------> quantas chaves
keys --------> iterável com chaves
values ------> iterável com valores
items -------> iterável com chaves e valores
setdefault --> adiciona valor se a chave não existe
copy --------> retorna uma copia rasa (shallow copy)
get ---------> obtém uma chave
pop ---------> apaga um item com a chave especificada (del)
popitem -----> apaga o ultimo item adicionado
update ------> atualiza um dicionário com outro

"""

import copy
pessoa = {
    'nome': 'Daniel',
    'sobrenome': 'Pinho'
}

print(len(pessoa))  # 2 chaves
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))
pessoa.setdefault('idade', None)
print(pessoa['idade'])

# Shallow Copy e Deep Copy

# Shallow copy: Cópia rasa

d1 = {
    'c1': 1,
    'c2': 2,
    'c3': [1, 2, 3, 4, 5]
}

d2 = d1  # aqui, d2 só vai apontar pro mesmo espaço na memória q d1
# Se eu alterar d2, d1 também vai alterar

d2 = d1.copy()  # aqui, d2 vai copiar d1
# Se eu alterar d2, apenas d2 vai alterar
# O problema é que, se tivermos valores mutáveis dentro da lista, ao invés de d2 copiar o valor do dado mutável de d1, d2 irá apontar pro espaço da memória que está guardado o dado mutável de d1, não sendo uma cópia completa, ou seja, se alterarmos o dado mutável em d2 (listas e dictionaries), o dado também será alterado em d1

d2['c3'][1] = 1000
print(d2['c3'])
print(d1['c3'])

# Deep copy: Cópia profunda

d2 = copy.deepcopy(d1)

# mesma coisa que o shallow copy, mas agora temos as variaveis apontando para diferentes lugares da memória em qualquer tipo de chave e qualquer tipo de atribuição às chaves, inclusive aos itens mutáveis.

d1['c3'][1] = 2
print(d1['c3'], d2['c3'])

# Get
# Evita erros no código. Com o get, se a chave que procurarmos não existir, ela retornará o valor NONE

try:
    print(d1.get('c1'))
    print(d1.get('nome', 'não existe'),
          ' <------ retornou None pois não existe \'nome\' no d1')
    print(d1('nome'))
except TypeError:
    print('deu Type Error pq não tem \'nome\' no d1')

# Pop
# apaga item de chave especificada

d2.pop('c3')

for chaves in d2:
    print(chaves, ':', d2[chaves])

# Pop Item
# apaga a ultima chave

d2.popitem()

for chaves in d2:
    print(chaves, ':', d2[chaves])

# Update
# atualiza chaves e pode até mesmo criar outras

d2.update({
    'c1': 'Chave 1 Atualizda.',
    'c2': 'Nova chave criada.',
    'c3': 'Mais uma chave criada.'
})

for chaves in d2:
    print(chaves, ':', d2[chaves])
