"""
Cuidados com dados mutáveis
sinal de = em mutáveis -----> aponta para o mesmo valor na memória
sinal de = em imutáveis ----> copia o valor
"""

# Exemplos IMUTÁVEIS:

a = 2
b = a
a = 3

print(a, b)
# o A muda de valor, mas o B continua com o valor antigo de A.
# Isso ocorre pois o B e o A, por serem imutáveis, faz com que o B apenas COPIE o valor de A e guarde para sí.

# Exemplos MUTÁVEIS:
a2 = [1, 2, 3]
b2 = a2
a2[0] = 'Olá mundo!'

print(a2, b2)
# o A2 muda de valor e, mesmo que isso ocorra DEPOIS do B2 já ter sido atrelado ao valor do A2, por estarmos fazendo estas operações com tipos MUTÁVEIS o B2 apenas APONTA pro mesmo local da memória que o A2 está apontando.
