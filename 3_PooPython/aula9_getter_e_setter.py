# @Property
# é um getter no modo pythonico (modo do python de fazer as coisas)
# @property é uma propriedade do objeto, ela é um metodo que se comporta como um atributo

# Geralmente é usada nas seguintes situações:
# Usada como getter
# P/ evitar de quebrar o código do cliente
# P/ habilitar setter
# P/ executar ações ao obter um atributo

# Código cliente
# é o codigo que usa o seu código
class Caneta:
    def __init__(self, cor):

        # No java, aqui usariamos os private, protected ou public, isso se chama encapsulamento

        # aqui no python não tem isso :(

        self._cor = cor
        # O que eu to falando quando boto o _ antes do cor ?
        # - Estou falando basicamente que este cor não deve ser usado. ->NÃO USE ESTE ATRIBUTO, ESTE ATRIBUTO É INTERNO DA CLASSE. SÓ DEVE SER USADO DENTRO DA CLASSE.<-

        # SE QUISERMOS QUE O CÓDIGO JÁ INSTANCIE COR COMO SETTER LOGO NO INÍCIO, BASTA QUE PASSEMOS O SELF.COR = COR QUE O >SELF.COR< SERÁ RECONHECIDO COMO O SETTER

        self.cor = cor
        self._cor_tampa = None
    # O PROPERTY faz com que o nosso método se comporte como atributo
    # ou seja, não conseguimos mais mexer com o verdadeiro atributo cor.
    # Ou seja(2), o property funciona BASICAMENTE como um getter

    @property
    def cor(self):
        print('GETTER PROPERTY')
        return self._cor

    @cor.setter  # ESTE É O MÉTODO SETTER
    def cor(self, valor):
        print('ESTOU NO SETTER, DEFINI A COR SENDO:', valor)
        self._cor = valor
    # def get_cor(self):

    #     # Usando o get agora o nosso atributo cor tá protegido
    #     print('GETTER COR PADRÃO')
    #     return self._cor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


#######################


caneta = Caneta('Azul')
# print(caneta.get_cor())
print(caneta.cor)
print(caneta.cor_tampa)
print()

caneta2 = Caneta('Vermelha')
# print(caneta2.get_cor())
print(caneta2.cor)
print(caneta2.cor_tampa)
print()

caneta3 = Caneta('Preta')
# print(caneta3.get_cor())
print(caneta3.cor)
print(caneta3.cor_tampa)
print()

caneta3.cor = 'Rosa'  # aqui usamos o setter
print(caneta3.cor)  # aqui usamos o getter

print('SEM O SETTER O SETTER')
print(caneta3.cor_tampa)
print('USEI O SETTER')
caneta3.cor_tampa = 'Rosa'
print(caneta3.cor_tampa)
