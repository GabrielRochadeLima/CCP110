codigo = float(input("Digite o código: "))


if(codigo == 1):
    classificacao = "ALimento não perecível"
    print(classificacao)
elif(codigo == 2 or codigo == 3 or codigo == 4):
    classificacao = "Alimento perecível"
    print(classificacao)
elif(codigo == 5 or codigo == 6):
    classificacao = "Vestuário"
    print(classificacao)
elif(codigo == 7):
    classificacao = "Higiene pessoal"
    print(classificacao)
elif(codigo >= 8 and codigo <=15):
    classificacao = "Limpeza e utensilios domésticos"
    print(classificacao)
else:
    print("Código inválido")
