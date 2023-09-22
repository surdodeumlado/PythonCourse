# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames

# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # str é melhor para maioria dos casos, onde a pessoa quer apenas ver uma string do seu objeto
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    # repr é melhor para desenvolvedores que querem entender como seu objeto é montado
    def __repr__(self) -> str:
        # class_name = self.__class__.__name__
        class_name = type(self).__name__  # é a mesma coisa q o de cima
        return f'{class_name}(x={self.x}, y={self.y})'

    def __add__(self, other):
        return 'bola'

    def __gt__(self, other) -> bool:
        resultado_self = self.x + self.y  # pegando a posição 1 e posição 2 do p1
        resultado_other = other.x + other.y  # pegando a posição 1 e posição 2 do p2
        return resultado_self > resultado_other


if __name__ == '__main__':

    p1 = Ponto(1, 2)
    p2 = Ponto(3, 4)
    p3 = p1 + p2
    print(p3)  # o metodo __add__ está retornando 'bola', print(p3) irá mostrar bola!

    print('P1 é maior que P2 ?', p1 > p2)
    print('P2 é maior que P1 ?', p2 > p1)

    print(p1, repr(p2))
    print(f'{p2!s}')  # str
    print(f'{p2!r}')  # repr
