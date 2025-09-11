# Uma granja classifica os ovos produzidos em pequeno e grande antes de embalá-los. Faça um programa que receba a medida dos ovos e os classifique seguindo a tabela a seguir:


# Tamanho	Classificação
# menor que 30 mm	pequeno
# maior ou igual a 30 mm	grande




# Por exemplo:

# Input	Resultado
# 35
# Digite a medida do ovo: 35
# grande
# 15.5
# Digite a medida do ovo: 15.5
# pequeno

medida_ovo= float(input("Digite a medida do ovo: "))

if(medida_ovo > 30):
    print("grande")
else:
    print("pequeno")
    
