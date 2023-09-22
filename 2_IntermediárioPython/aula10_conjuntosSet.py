# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# parecem dicionários, mas não tem chaves e valor, tem apenas valor
s1 = set()  # Só assim para criar um set vazio. {} cria um dicionário vazio
print(s1, type(s1))
# Dá pra criar set assim também, mas tem que obrigatoriamente passar valor
s2 = {1, 2, 3}

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# - Eliminam valores repetidos
s3 = {1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 1}
print(s3)

lista = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 1, (123,)]
s4 = set(lista)
print(s4)
listaTransformada = list(s4)
print(listaTransformada)

# Remove permanentemente os elementos duplicados

for numero in lista:
    print(numero, end=' ')
print()

for numero in s4:
    print(numero, end=' ')

print(f'\n{3 in s4}')
print(4 not in s4)

# Métodos úteis:
# add, update, clear, discard

# - Add: adiciona valores ao set

s4.add(4)
print(s4)

# - Update: atualiza o set com o novo valor passado.
# - Observação: No set, tudo vem de forma iterada, então se passarmos umas String, cada letra dela será 1 elemento

s4.update('Olá mundo!')
print(s4)
# Se quisermos passar uma palavra completa, sem estar iterada, mandamos dentro de parênteses

# podemos mandar varios valores no update
s4.update(('Olá mundo!', 1, 2, 3, 4))
print(s4)

# - Discard: descartamos um elemento de dentro do nosso set

# Passamos o próprio elemento como parâmetro e não sua posição
s4.discard(('Olá mundo!'))
s4.discard('Olá mundo!')

print(s4)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

ss1 = {1, 2, 3}
ss2 = {2, 3, 4}
ss3 = s1 | s2  # Une s1 e s2
print(ss3)
ss3 = s1 & s2  # Mostra itens presentes em ambos
print(ss3)
ss3 = s1 - s2  # Itens presentes apenas no set da esquerda
print(ss3)
ss3 = s1 ^ s2  # Itens que não estão presentes em todos os sets 
print(ss3)
