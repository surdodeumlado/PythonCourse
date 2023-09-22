"""

Flag(bandeira) -----> Marcar um local
none ---------------> Não valor
is e is not --------> é ou não é (tipo, valor, identidade)
id -----------------> identidade

"""


condicao = False
passouNoIf = None

if condicao:
    passouNoIf = True  # essa é a flag, vai identificar se passamos ou n dentro do if
    print('Faça algo')
else:
    print('Não faça algo')

print(passouNoIf, passouNoIf is None)
print(passouNoIf, passouNoIf is not None)
