string = 'ABCD'
lista = ['Maria', 'Daniel', (1, 2, 3), 'Eduarda']
tupla = 'Python', 'Java', 'PHP'

a, b, *_, c = lista

print(a, b, c)
# O asterístico significa que iremos passar no print cada elemento de dentro da string
print(*string)
# Também funciona com tuplas
print(*tupla)
