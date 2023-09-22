"""
Interpolação basica de strings
s --------> String
d ou i ---> int
f --------> float
x ou X ---> hexadecimal(ABCDEF1234567890) P.S.: x minúsculo = hexadecimal minúsculo, X maiúsculo = 
            hexadecimal maiúsculo
"""

nome = 'Luiz'
preco = 1000.2103912031820
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
# a interpoçação é estes % que vem dentro das aspas, para chamarmos as variaveis que apareceram ali dentro a gente coloca % como sufixo após as aspas e passamos dentro de parênteses as variaveis. P.S.: Se for apenas 1 variavel n precisa de parênteses

print(variavel)
