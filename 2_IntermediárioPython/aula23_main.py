from sys import path
# # import aula23_package -----> se importar só package não vai dar em nada, pq não vamos estar importando os modulos dentro dele

# # import aula23_package.modulo -----> também daria pra fazer assim, MAS iria importar TUDO do modulo e ficaria com uma sintaxe gigante

# # from aula23_package import modulo -----> também dá pra fazer assim, mas também importaria tudo do modulo, com o único porém que a sintaxe iria ficar mais amigável

# from aula23_package.modulo import soma_do_modulo

# # MÁ PRÁTICA:
# from aula23_package.modulo import *

# # maneira correta de se importar

# # print(*path, sep='\n')

# print(soma_do_modulo(1, 8))
# print(variavel)  # importada por conta do all (*)

import aula23_package
