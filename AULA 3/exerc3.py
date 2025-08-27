dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

dias_s= dias*24*60*60
horas_s= horas*60*60
minutos_s= minutos*60

conversao = dias_s+horas_s+minutos_s+segundos

print(f"Tempo total foi de: {conversao} segundos")
