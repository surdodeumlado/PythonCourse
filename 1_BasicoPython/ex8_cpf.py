cpf = '671055482'
# Calculo 1° dígito

fatiamento_do_cpf_1 = cpf[:9]
contagem_regressiva_indice = 11
soma_de_indices = 0

for indice in fatiamento_do_cpf_1:
    contagem_regressiva_indice -= 1
    soma_de_indices += int(indice) * contagem_regressiva_indice

penultimo_indice = (soma_de_indices * 10) % 11
resultado_primeiro_digito = 0 if penultimo_indice > 9 else penultimo_indice

# Calculo do 2° digito

fatiamento_do_cpf_2 = cpf[:10]
soma_de_indices = 0
contagem_regressiva_indice = 11

for indice in fatiamento_do_cpf_2:
    soma_de_indices += int(indice) * contagem_regressiva_indice
    contagem_regressiva_indice -= 1

ultimo_indice = (soma_de_indices * 10) % 11
resultado_segundo_digito = 0 if ultimo_indice > 9 else ultimo_indice

print(
    f'Os últimos 2 digitos do CPF são {resultado_primeiro_digito} e {resultado_segundo_digito}')

novo_cpf = f'{fatiamento_do_cpf_1}{resultado_primeiro_digito}{resultado_segundo_digito}'

print(novo_cpf)
