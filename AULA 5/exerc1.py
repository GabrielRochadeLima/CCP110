preco = float(input("Digite o preço do produto: "))
codigo = float(input("Digite o código: "))


if(codigo == 1):
    procedencia = "Sul"
elif(codigo == 2):
    procedencia = "Norte"
elif(codigo == 3):
    procedencia = "Leste"
elif(codigo == 4):
    procedencia = "Oeste"
elif(codigo == 5 or codigo ==6):
    procedencia = "Nordeste"
elif(codigo == 7 or codigo == 8 or codigo == 9):
    procedencia = "Sudeste"
elif(codigo >= 10 and codigo <=20):
    procedencia = "Centro-oeste"
elif(codigo >= 25 and codigo <=30):
    procedencia = "Nordeste"
else:
    procedencia = "Importado"

print(f"O produto custa {preco:.2f} e é originado do(a) {procedencia}.")