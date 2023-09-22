"""
INTRODUÇÃO AO TRY/EXCEPT
try -----> tentar executar o código
except --> ocorreu algum erro ao tentar executar

tenta executar algum código, caso ocorra algum erro voce captura o erro
"""

numero_str = input('Vou dobrar ')
print(numero_str.isdigit())

try:  # tentando executar expressão
    numero_float = float(numero_str)
    print(f'O dobro do número é {numero_float * 2}')
except:  # o except, se era pra dar erro no código executa o código q passarmos
    print('Não é um número')

# se a excessão ocorre dentro do try, ele pula automaticamente pro except.
