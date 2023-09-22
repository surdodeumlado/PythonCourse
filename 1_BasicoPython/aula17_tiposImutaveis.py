# tipos imutaveis que vimos até agora: int, str, float, bool

string = 'Daniel pinho'
# string[3] = 'ABC'  -----> isso vai dar um erro pois a string é IMUTAVEL
# pra mudarmos os valores temos que criar outra variável

novaString = f'{string[:3]}ABC{string[4:]}'
print(novaString)
# Assim conseguimos mudar uma string sem de fato alterar a variável original.

# existem vários métodos que podemos manipular strings sem alterar a variável original, podemos ver na documentação do python
# https://docs.python.org/3/library/stdtypes.html
