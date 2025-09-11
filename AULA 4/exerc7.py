distancia = float(input("Digite a distancia que você quer percorrer em km: "))
if (distancia <= 200):
    valor_passagem = distancia * 0.5

else:
    valor_passagem  = 200 * 0.5 + (distancia- 200) * 0.45
print(f"O valor da passagem é: {valor_passagem:.2f}")
    
