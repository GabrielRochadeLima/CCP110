# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo (todos números inteiros). A seguir calcule a duração do jogo.

# O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

 

 

# Por exemplo:

# Input	Resultado
# 7
# 8
# 9
# 10
# Digite a hora inicial: 7
# Digite o minuto inicial:8
# Digite a hora final: 9
# Digite o minuto final: 10
# O jogo durou 2 hora(s) e 2 minutos(s)
# 23
# 55
# 5
# 27
# Digite a hora inicial: 23
# Digite o minuto inicial:55
# Digite a hora final: 5
# Digite o minuto final: 27
# O jogo durou 5 hora(s) e 32 minutos(s)

hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite o minuto inicial:"))
hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite o minuto final: "))

minutos_inicio = (hora_inicial * 60) + minuto_inicial
minutos_final = (hora_final * 60) + minuto_final

duracao_em_minutos = minutos_final - minutos_inicio
if duracao_em_minutos <= 0:
    duracao_em_minutos += 1440

horas_jogo = duracao_em_minutos // 60
minutos_jogo = duracao_em_minutos % 60

print(f"O jogo durou {horas_jogo} hora(s) e {minutos_jogo} minutos(s)")