"""
Closure e funções que retornam outras funções
"""


# def criar_saudacao(saudacao, nome):
#     return f'{saudacao}, {nome}'


# s1 = criar_saudacao('Bom dia', 'Luiz')

# print(s1)

# Por questões de praticidade, se eu quiser criar varias saudações, pra não ter que ficar repetindo varias linhas de texto com o mesmo comando ou argumento sendo passado, podemos utilizar das closures

def criar_saudacao(saudacao):  # Mesmo que passarmos os mesmos argumentos em 2 variáveis diferentes callando essa mesma função, as 2 variáveis apontaram pra lugares distintos da memória
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa Noite')

for nome in ['Daniel', 'Pedro', 'Arthur', 'Cauê', 'Marcus']:
    print(falar_bom_dia(nome), end='. ')

print()

for nome in ['Daniel', 'Pedro', 'Arthur', 'Cauê', 'Marcus']:
    print(falar_boa_noite(nome), end='. ')
