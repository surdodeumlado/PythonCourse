"""
INTRODUÇÃO AO DESEMPACOTAMENTO
É quando desempacotamos uma lista e passamos seus valores para variáveis.
"""
nomes = ['Daniel', 'João', 'Maria', 'Pedro']
nome1, nome2, nome3, nome4 = nomes

print(nome1)
print(nome2)
print(nome3)
print(nome4)

# Se não tiver variável suficiente pra preencher os nomes, o código dará um erro
# nome1, nome2, nome3 = ['Daniel', 'João', 'Maria', 'Pedro'] <--------- Daria um erro por ter 3 variáveis para 4 nomes

# Se tiver mais variável do que nome, também dará um erro
# nome1, nome2, nome3, nome4, nome5 = nomes <-------------------------- Daria um erro por ter 5 variáveis para 4 nomes

# Se quisermos desempacotar os valores mas não tivermos variáveis o suficiente, podemos criar uma variável com * no início, que desempacotará todo o resto pra nós

nome_Daniel, *resto = nomes
print(nome_Daniel, resto)

# Se não quisermos utilizar a variável mais pra frente, por convenção e padronização nós botamos o nome da variável como underline '_'
# A variável *_ funciona igual uma variável normal, porém por ela estar com o nome *_ significa que nós n usamos ela em momento algum do código, a n ser para descartar o resto

nome_Daniel2, *_ = nomes
print(nome_Daniel2)

# Se utilizarmos uma variável de resto ao final do código, mesmo com todos os elementos já tendo sido desempacotados, ainda sim a variável funcionará, porém ela receberá uma lista vazia.

nomee_daniel, nomee_joao, nomee_maria, nomee_pedro, *resto = nomes
print(nomee_daniel, nomee_joao, nomee_maria, nomee_pedro, resto)

# -------------------------------------------------------------------------- #

"""
INTRODUÇÃO ÀS TUPLAS
É uma lista, só que com valores imutáveis
Usamos quando criarmos uma lista que não queiramos mudar, remover, etc os valores.
"""

# A sintaxe da tupla é quase a mesma das listas, a diferença é que as tuplas não possuem colchetes

listaNumeros = 1, 2, 3, 4  # É uma tupla.

# Se quisermos ser MUITO específicos, ao invés de criar a tupla sem nada, nos criamos com parênteses

listaNumeros2 = (1, 2, 3, 4)  # Também é uma tupla.

# Chamar valores específicos de uma tupla é da mesma maneira que chamariamos a de uma lista
print(listaNumeros2[2])
