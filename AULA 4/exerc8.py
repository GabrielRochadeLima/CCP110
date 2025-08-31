from math import ceil

altura = float(input("Digite a altura a ser pintada: "))
raio = float(input("Digite o raio a ser pintada: "))

area_base = 3.1415 * raio**2
perimetro = 2 * 3.1415 * raio
area_lateral = altura * perimetro
area_cilindro = area_base + area_lateral

area_lata = 15
qtd_lata= ceil(area_cilindro/area_lata)

litros = area_cilindro/3

if (qtd_lata == 1):
    valor_lata = 50

elif(qtd_lata == 2):
    valor_lata = 48

elif(qtd_lata == 3):
    valor_lata = 46
else:
    valor_lata = 45

custo_total = valor_lata*qtd_lata

print (f"A area para ser ser pintada é {area_cilindro:.2f}")
print(f"Quantidade de litros de tinta necessário é: {litros:.2f}")
print(f"Quantidade de latas de tinta é: {qtd_lata:.2f}")
print(f"Preço unitário da lata: {valor_lata:.2f}")
print(f"Custo total {custo_total:.2f}")