# isso é bom para por um intervalo de números dentro do for

numeros = range(10)
print(numeros)  # range de 0 à 10
numeros = range(5, 10)
print(numeros)  # range de 5 à 9
numeros = range(10, 0, -1)
print(numeros)  # range de 10 a 1 regredindo de 1 em 1

for numero in numeros:
    # para cada numero dentro da variável numeros, ele vai jogar um valor pra dentro da variável numero
    print(numero)
