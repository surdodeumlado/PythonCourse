# No python nós não temos o conceito de variaveis constantes
# Para contornar este problema, é consenso geral que variáveis digitadas inteiramente em
# letras maiúsculas, são variáveis que não vão mudar de valor.

velocidade = 61  # velocidade em que o carro está atualmente
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # a distância onde o radar pega

# muitas condições em um mesmo IF também é uma má prática
# muitos blocos de código é ruim também (os tabs que a gente dá no inicio da linha)
# simples > complexo, explicito > implicito

vel_carro_pasosu_radar_1 = velocidade > RADAR_1

multar_carro_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = multar_carro_radar_1 and vel_carro_pasosu_radar_1

if vel_carro_pasosu_radar_1:
    print('Velocidade Excedida.')
if carro_multado_radar_1:
    print('Carro multado em radar 1')
