# Uma loja está fazendo uma promoção para clientes que comprem três produtos. Ler o valor de cada produto e calcular o valor total da compra. Caso o total da compra seja acima de R$ 500,00 ele terá 20% de desconto, senão o desconto será de 10%. Calcular e mostrar o desconto para um cliente (considere duas casas decimas na saída).

# Por exemplo:

# Input	Resultado
# 10
# 20
# 30
# Digite o valor do primeiro produto: 10
# Digite o valor do segundo produto: 20
# Digite o valor do terceiro produto: 30
# Desconto: 6.00
# 200
# 300
# 100
# Digite o valor do primeiro produto: 200
# Digite o valor do segundo produto: 300
# Digite o valor do terceiro produto: 100
# Desconto: 120.00

valor1 = float(input("Digite o valor do primeiro produto: "))
valor2 = float(input("Digite o valor do segundo produto: "))
valor3 = float(input("Digite o valor do terceiro produto: "))

compra = valor1 + valor2 + valor3

if(compra > 500):
    desconto = compra * 0.20
else:
    desconto = compra * 0.10
print(f"Desconto: {desconto:.2f}")    
