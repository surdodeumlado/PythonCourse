"""
  0 1 2 3 4 5 6 7 8 9
  o l a   m u n d o !
-10-9-8-7-6-5-4-3-2-1 

fatiamento [i:f:p]
i ----> inicio
f ----> fim
p ----> passo (andar de tantos em tantos numeros)
[::]
Obs.: A função len retorna a quantidade de caracteres, inclusive espaços

"""

frase = 'Odeio comer manjericão'
print(frase[::3])
print(frase[:-17:])
print(len(frase))  # índices começa do 0, caracteres começam do 1
