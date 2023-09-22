frase = 'sabia que o sabio soube que o sabia sabia assobiar ?'

i = 0
cont = 0
letra = ''
while i < len(frase):
    conte = frase.count(frase[i])
    if conte > cont and frase[i] != ' ':
        cont = conte
        letra = frase[i]
    i += 1

print(f'O caractere \'{letra}\' apareceu {cont} vezes.')
