"""
Escopo das funções em python
Escopo: o local onde aquele código pode aringir
Escopo global: é o local onde todo código pode ser alcançado
"""

x = 1


def escopo():
    global x  # esse é o x = 1 fora da função
    x = 10  # variável local
    # Após chamarmos o global x e atribuir 10 ao valor de x, ao invés deste x ser a variável local, ele passará a mudar o valor REAL do X de FORA da função, então o x global também passará a ser 10

    def escopoInterno():
        x = 11  # mais uma variável local
        y = 9
        print(x, y)
    escopoInterno()
    print(x)


escopo()
print(x)
