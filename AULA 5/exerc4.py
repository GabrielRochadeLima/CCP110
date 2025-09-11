ano_nasciemnto=int(input("Digite seu ano de nascimento: "))

idade = 2025-ano_nasciemnto

if(idade >=18):
    print("Você pode tirar a CNH e votar")
elif(idade >=16):
    print("Você pode votar, mas não pode tirar a CNH") 
else:
    print("Você não pode votar e nem tirar a CNH")