"""
while (enquanto)
executa uma ação enquanto ela for verdadeira
"""

cont = 0
while cont <= 3:
    print(1)
    print(2)
    print(3)
    cont += 1

# podemos por um laço dentro do outro

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha = }, {coluna = }')
        coluna += 1
    linha += 1
