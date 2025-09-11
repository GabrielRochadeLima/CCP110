genero = input("Digite o seu genero (M/F): ")
altura = float(input("Digite a sua altura em metros: "))


if(genero == "M"):
    peso_ideal = (72.7*altura)-58
    print(f"Seu peso ideal é {peso_ideal}")
elif(genero == "F"):
    peso_ideal = (62.1*altura)-44.7
    print(f"Seu peso ideal é {peso_ideal}")
else:
    print("Genênero inválido")    