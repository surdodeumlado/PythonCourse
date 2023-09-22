"""
Formatação basica de strings
s --------> String
d --------> int
f --------> float
.<numero de dígitos>f
x ou X ---> hexadecimal(ABCDEF1234567890) P.S.: x minúsculo = hexadecimal minúsculo, X maiúsculo = 
            hexadecimal maiúsculo
(Caractere)(><^)(quantidade)
> --------> esquerda
< --------> direita
^ --------> centro
sinal ----> + ou -
Ex.: 0>-100,.1f
Conversion flags -> !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:0^10}')
print(f'{1000.190238102938102938:,.2f}')
