dia= int(input("Digite a quantidade de dias que quer alugar o carro: "))
km= float(input("Digite a quantidade de km rodado: "))

total = (km*0.15)+(dia*60)

print(f"Você precisa pagar: R$ {total:.2f}")