# <valor> if <condição> else <outro valor>

variavel = 'Valor' if True else False

print(variavel)

condicao = 10 == 10
variavel2 = 'Verdadeiro' if condicao else 'falso'

print(variavel2)

digito = 1  # > 9 = 0
novo_digito = digito if digito <= 9 else 0  # condição normal
print(novo_digito)

digito = 10
novo_digito = 0 if digito > 9 else digito  # condição invertida
print(novo_digito)
