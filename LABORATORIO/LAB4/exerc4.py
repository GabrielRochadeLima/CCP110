# # Uma loja dá desconto de 10% para compras à vista, 5% para compras em 2 ou 3 parcelas e não dá desconto para compras acima de 3 parcelas. Além disso, a loja dá mais 5% de desconto (você pode somar essa porcentagem ao outro possível desconto) aos clientes que comprarem um total superior a R$5.000,00. Faça um programa para ler o valor da compra e o número de parcelas, calcular e mostrar o valor do desconto,  o valor final da compra com desconto e o valor de cada parcela. Utilize duas casas decimais.
# Input	Resultado
# 500.40
# 2
# Digite o valor da compra: 500.40
# Digite a quantidade de parcelas: 2
# Desconto total: 25.02
# Valor final da compra com desconto: 475.38
# Cada parcela será de: 237.69
# 10000.00
# 3
# Digite o valor da compra: 10000.00
# Digite a quantidade de parcelas: 3
# Desconto total: 1000.00
# Valor final da compra com desconto: 9000.00
# Cada parcela será de: 3000.00
# 8000.25
# 1
# Digite o valor da compra: 8000.25
# Digite a quantidade de parcelas: 1
# Desconto total: 1200.04
# Valor final da compra com desconto: 6800.21
# Cada parcela será de: 6800.21
# 15000.00
# 4
# Digite o valor da compra: 15000.00
# Digite a quantidade de parcelas: 4
# Desconto total: 750.00
# Valor final da compra com desconto: 14250.00
# Cada parcela será de: 3562.50

valor_compra = float(input("Digite o valor da compra: "))
num_parcelas = int(input("Digite a quantidade de parcelas: "))

desconto = 0

if num_parcelas == 1:
    desconto = valor_compra * 0.10
elif num_parcelas == 2 or num_parcelas == 3:
    desconto = valor_compra * 0.05

if valor_compra > 5000:
    desconto = desconto + (valor_compra * 0.05)

valor_final = valor_compra - desconto
valor_parcela = valor_final / num_parcelas

print(f"Desconto total: {desconto:.2f}")
print(f"Valor final da compra com desconto: {valor_final:.2f}")
print(f"Cada parcela será de: {valor_parcela:.2f}")