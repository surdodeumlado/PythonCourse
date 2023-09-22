# Relações entre classes: associação, agregação e composição

# Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos

# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.

# A associação não especifica como um objeto controla o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property  # Getter
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter  # Setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome) -> None:
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo.'


escritor = Escritor('Daniel')
caneta = FerramentaDeEscrever('Caneta Bic')
escritor.ferramenta = caneta  # assim que linkamos 2 objetos

print(caneta.escrever())
print(escritor.ferramenta.escrever())

maquina_de_escrever = FerramentaDeEscrever('Maquina de Escrever')
escritor.ferramenta = maquina_de_escrever
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())
