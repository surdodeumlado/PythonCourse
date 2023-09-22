def multiplicando(numero):
    def multiplicador(multiplicador):
        return numero * multiplicador
    return multiplicador


duplicando = multiplicando(2)
triplicando = multiplicando(3)
quadriplicando = multiplicando(4)

print(duplicando(2))
print(triplicando(3))
print(quadriplicando(4))
