codigo = float(input("Digite o código: "))


if(codigo == 1):
    classificacao = "ALimento não perecível"
elif(codigo == 2 or codigo == 3 or codigo == 4):
    classificacao = "Alimento perecível"
elif(codigo == 5 or codigo == 6):
    classificacao = "Vestuário"
elif(codigo == 7):
    classificacao = "Higiene pessoal"
elif(codigo >= 8 and codigo <=15):
    classificacao = "Limpeza e utensilios domésticos"
else:
    print("Código inválido")
