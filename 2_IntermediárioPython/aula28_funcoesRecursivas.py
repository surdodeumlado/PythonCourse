# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm


def recursiva(inicio=0, fim=10):
    # caso base
    if inicio >= fim:
        return fim

    print(inicio, fim)

    # caso recursivo
    # contar até chegar no final
    inicio += 1
    return recursiva(inicio, fim)
# basicamente fizemos um laço


print(recursiva())


def fatorial(n):

    if n == 0 or n == 1:
        return 1

    return n * fatorial(n - 1)


# basicamente fizemos um for
print(fatorial(5))

e = 1
num = 5
while num > 0:
    e *= num
    num -= 1
print(e)
