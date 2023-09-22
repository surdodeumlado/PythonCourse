# Comentários

"""
Isso aqui não é comentário, mas alguns desenvolvedores usam como comentário multilinha
agora posso pular linhas
o python lê isso aqui diferente dos comentários.
"""

# por padrão o python pula 1 espaço entre 2 argumentos
print("Olá",  "mundo!", sep="-")
# para evitar isso, usamos o sep='', dentro das aspas colocamos o quê queremos
# que apareça entre os 2 argumentos
print("Olá",  "mundo!")
# A quebra de linha se faz com o \r\n (windowns mais antigos) ou \n (sistemas mais novos)
print("Olá\nmundo!")
# Se não quisermos quebra de linha, podemos colocar o ,end='' para o print de baixo vir com o de cima
print("Olá mundo!", end=' ')
print("Olá mundo!")
