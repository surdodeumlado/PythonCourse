import aula27_b_uma_linha as uma_linha
import aula27_c_varias_linhas as varias_linhas
import aula27_d_funcao_com_doc as funcao_nas_linhas
import aula27_e_classe_com_doc as class_nas_linhas

print(dir(uma_linha))  # vai mostar tudo que tem ali no modulo
# usando os metodos dunder dá pra ver diretamente oq é cada coisa do uma_linha
print(uma_linha.__name__)  # nome do modulo
print(uma_linha.__doc__)
print(uma_linha.__file__)  # caminho do arquivo
print(uma_linha.__package__)

print(help(varias_linhas))
print(help(funcao_nas_linhas))
print(help(class_nas_linhas))
