import sys

import aula21_modulos_m
from aula21_modulos_m import variavel_modulo

# modulos proprios do python
# primeiro modulo executado: __main__
# dá pra importar outro módulo inteiro ou parte do modulo
# o python conhece a pasta onde o __main__ está e as pastas abaixo dele
# ele não reconhece as pastas acima do __main__ por padrão
# o python conhece todos os modulos e pacotes presentes nos caminhos sys.path

# print(f'Este modulo se chama {__name__}')
# print(*sys.path, sep='\n')

print(aula21_modulos_m.variavel_modulo)
print(variavel_modulo)
