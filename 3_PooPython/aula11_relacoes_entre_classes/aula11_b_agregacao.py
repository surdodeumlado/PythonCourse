# Relações entre classes: associação, agregação e composição

# Agregação é uma forma mais especializada de associação entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.

# Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.

# Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.

# (existem controvérsias sobre as definições de agregação).

# Em resumo, agregação é UM TIPO de associação, uma classe consegue viver sem outra, mas as 2 juntas formam algo maior

# Exemplo: Um carro consegue viver sem roda, uma roda consegue viver sem carro, mas um carro com rodas é bem melhor e mais completo.

class CarrinhoCompras:
    def __init__(self) -> None:
        self._produtos = []

    def inserir_no_carrinho(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco


carrinho = CarrinhoCompras()
p1, p2 = Produto('Caneta', 1.20), Produto('Cereal', 12.50)

carrinho.inserir_no_carrinho(p1, p2)

carrinho.listar_produtos()
print(carrinho.total())
