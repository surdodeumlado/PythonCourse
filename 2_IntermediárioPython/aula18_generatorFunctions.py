# Generator functions são funções que sabem pausar

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return


gen = generator(n=0)

# print(next(gen))  # mais um next e vai nos retornar o próximo yield
# print(next(gen))  # mais um next e vai nos retornar o próximo yield
# print(next(gen))  # mais um next e vai nos retornar o próximo yield

for n in gen:
    print(n)
