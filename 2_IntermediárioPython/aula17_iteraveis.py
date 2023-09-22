import sys

# Generator expression, iterables e iterators em python

# Iterator ====================================================================================================

# iterável ----> item sequencial q voce pode acessar as coisas sequencialmente
# iterator ----> a unica responsabilidade do iterator é te entregar 1 valor por vez, ou seja, ele só vai te entregar o próximo valor. Ele não sabe o primeiro, o ultimo, o anterior, nada do tipo, apenas o próximo da lista.

# Iterator é uma classe que tem que trabalhar com os métodos __iter__ e o método __next__ e com uma variável iterável pra poder funcionarem.

iterable = ['eu', 'tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__

for i in iterable:
    print(next(iterator))

# Se tentarmos puxar o next mais uma vez, dá um erro de stop iterator, que já acabou o iterator
try:
    print(next(iterator))
except StopIteration:
    print('Erro de StopIteration')


# Generator ===================================================================================================
# são funções que sabem pausar em determinada ocasião
# Todo generator também é um iterator. Dá pra usar o for, pedir next, etc
# MAS um iterator NÃO É um generator.

lista = [n for n in range(100000)]  # ---------> isso é um list comprehension
generator = (n for n in range(100000))  # -----> isto é um generator

print(sys.getsizeof(lista))  # Na lista, os valores já foram salvos na memória
print(sys.getsizeof(generator))  # no generator, não

print(next(generator))  # Ele vai mostar 1 valor e pausar.
print(next(generator))  # Ele vai mostar 1 valor e pausar.
print(next(generator))  # Ele vai mostar 1 valor e pausar.
print(next(generator))  # Ele vai mostar 1 valor e pausar.
print(next(generator))  # Ele vai mostar 1 valor e pausar.
print(next(generator))  # Ele vai mostar 1 valor e pausar.
