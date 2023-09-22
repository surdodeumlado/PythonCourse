import importlib

import aula21_modulos_m

# recarregando módulos -----> Não é muito usado, mas existe essa possibilidade
# singleton ----------------> Só pode existir uma instancia de tal coisa, os import são singleton por exemplo
# import lib ---------------> funções que operam sob bibliotecas ou importações

print(aula21_modulos_m.variavel_modulo)

for i in range(1, 11):
    # estamos recarregando o módulo 10 vezes, ou seja, se tiver um código padrão lá ele aparecerá no console 10 vezes
    importlib.reload(aula21_modulos_m)
    print(i)

print('fim')
