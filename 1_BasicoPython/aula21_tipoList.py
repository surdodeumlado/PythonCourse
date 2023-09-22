"""
Listas são valores mutáveis, podem ser mudados
Suportam qqr valor de qqr tipo
Se a lista estiver vazia, ela repassará em bool o valor FALSE, se estiver com itens, ela repassará o valor TRUE
"""

string = 'ABCDE'
lista = list()  # uma das maneiras de se escrever listas, usado mais quando eh um type conversion
lista2 = ['A', 'B', 'C', 'D', 'E']  # maneira comum de se escrever lista

# --------0----1---------------2-----3----4---------
lista3 = [123, 'Daniel Pinho', True, 1.2, [1, 2, 3]]
# ------'-5'-'-4'------------'-3'--'-2'-'-1'--------

print(lista3[1])
lista3[1] = 'Daniel Vale'
print(lista3[1])

# MÉTODOS ÚTEIS:
# append -------> Adiciona valores ao final da lista. Ex.: lista3.append(50) -> valor 50 adicionado ao final
# insert -------> Adiciona valor no índice escolhido. Ex.: lista3.insert(indice q iremos mexer, valor do indice)
# pop ----------> Remove o elemento FINAL da lista. Ex.: lista3.pop() -> o elemento [1, 2, 3] foi deletado
# del ----------> Deleta elemento de posição repassada. Ex.: del lista3[3] -> removeria o 1.2
# clear --------> Limpa a lista por completo. Ex.: lista.clear(0)
# extend -------> Estende a lista. Ex.: lista_a.extend(lista_b)
# + ------------> Concatena listas. Ex.: lista_a = lista_b + lista_c
# P.S.: O extend faz a ação, mas n entrega o dado de volta. Ou seja, diferente do + que vai concatenar as 2 listas e a lista_a agora vai ser a lista_b concatenada com a lista_c, no extend a lista_a vai EXTENDER a lista_b, ou seja ela vai ser mudada.

# Obs.: Não é interessante deletar elementos do MEIO da lista se ela for mto grande, vai requerer muito processamento pra mover todos os itens de lugar.
