def multiplicador(*args):
    total = 1
    for elementos in args:
        total *= elementos
    return total


print(multiplicador(-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1))


def parOuImpar(x):
    if x % 2 == 0:
        return 'Par'  # quando return é atingida, sai da função, por isso n tem o else
    return 'Impar'


print(parOuImpar(2))
print(parOuImpar(3))
