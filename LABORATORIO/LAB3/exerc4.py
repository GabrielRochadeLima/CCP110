
# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

# Por exemplo:

# Input	Resultado
# 2
# 10
# Digite o código do produto:2
# Digite a quantidade do produto:10
# Total: R$ 65.00
# 3
# 7
# Digite o código do produto:3
# Digite a quantidade do produto:7
# Total: R$ 35.00

codigo = int(input("Digite o código do produto:"))
qtd = int(input("Digite a quantidade do produto:"))

if(codigo == 1):
    preco = 6
elif(codigo == 2):
    preco = 6.50
elif(codigo == 3):
    preco = 5
elif(codigo == 4):
    preco = 3
elif(codigo == 5):
    preco = 2
else:
    print("Numero invalido, digite um ncodigo de 1 a 5")
    
total = preco*qtd
print(f"Total: R$ {total:.2f}")