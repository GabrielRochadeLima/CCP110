# # Faça um programa para exibir a idade de uma pessoa tendo como entrada a sua faixa etária, de acordo com a tabela abaixo: 
# Faixa etária	Idade
# Bebê	menor que 2 anos
# Criança	de 3 a 10 anos
# Adolescente	de 11 a 17 anos
# Adulto	de 18 a 64 anos
# Idoso	maior que 65 anos
idade = input("Digite a faixa etária: ")

if(idade == "Bebê"):
    print("menor que 2 anos")
elif(idade == "Crincça"):
    print("de 3 a 10 anos")
elif(idade == "Adolescente"):
    print("de 11 a 17 anos")
elif(idade == "Adulto"):
    print("de 18 a 64 anos")
elif(idade == "Idoso"):
    print("maior que 65 anos")