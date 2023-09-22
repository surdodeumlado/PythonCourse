# empacotamento e desempacotamento normalmente

lista = [1, 2, 3, 4, 5, 6]
a, b, c, *_ = lista

print(a, b, c, _)

# empacotamento e desempacotamento em chaves

pessoa = {
    'nome': 'Daniel',
    'sobrenome': 'Pinho',
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.70,
}

# EMPACOTAMENTO ===============================================================================================

# # a, b = pessoa
# # print(a, b) -----> vai retornar 'nome' e 'sobrenome' (as chaves)

# # a, b = pessoa.values()
# # print(a, b) -----> vai retornar 'Daniel' e 'Pinho' (os valores)

# # a, b = pessoa.items()
# # print(a, b) -----> vai retornar '(nome, 'Daniel'), (sobrenome, 'Pinho')' (tuplas com chave e valor)

# # (a1, a2), (b1, b2) = pessoa.items()
# # a1 e b1 = chaves, a2 e b2 = valores
# """
# for chave, valor in pessoa.items():
#     print(chave, valor) ----------> vai printar na tela tanto as chaves quanto os valores
# """

# DESEMPACOTAMENTO ============================================================================================

# # dá pra criar um 3° dicionario e juntar os 2

pessoa_completa = {
    **pessoa,
    'chave': 1,
    **dados_pessoa,
}

print(pessoa_completa)

# # vai resultar em um dict com dados dos dicts pessoa, dados pessoa e a chave: 1 que passamos ali

# KWARGS ======================================================================================================

# keyword arguments, são os tais dos argumentos nomeados


def mostro_argumentos_nomeados(*args, **kwargs):  # kwargs sempre usam **
    for elemento in args:
        print(elemento)

    for chave, valor in kwargs.items():
        print(f'{chave=}, {valor=}')


# Vai retornar um dicionário pra gente com os argumentos que passamos
mostro_argumentos_nomeados('Daniel (não nomeado)', 'Pinho (não nomeado)',
                           nome='Daniel', sobrenome='Pinho', idade=18, altura=1.70)

# Os argumentos não nomeados que passarmos serão os args, os argumentos NOMEADOS que passarmos serão os kwargs
