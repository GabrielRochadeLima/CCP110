ano_atual = int(input("Digite o ano atual: "))
data_nasc = int(input("Digite o ano de nascimento: "))

idade = ano_atual - data_nasc

if(idade > 18):
    print("Parabens! voce pode tirar a CNH")
else:
    print("Você é menor de idade, não pode tirar a CNH")