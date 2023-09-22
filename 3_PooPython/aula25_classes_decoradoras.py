# classes decoradoras (decorator classes)

from typing import Any


class Multiplicar:
    def __init__(self, func) -> None:
        self.func = func
        self._z = 10

    def __call__(self, *args, **kwargs) -> Any:
        resultado = self.func(*args, **kwargs)
        return resultado * self._z


@Multiplicar
def soma(x, y):
    return x + y


dois_mais_dois = soma(2, 2)
print(dois_mais_dois)
