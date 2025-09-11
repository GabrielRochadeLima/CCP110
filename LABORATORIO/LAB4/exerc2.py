# Escreva um programa que determine o nome de uma forma a partir de seu número de lados. Leia o número de lados do usuário e relate o nome apropriado como parte de uma mensagem significativa. Seu programa deve oferecer suporte a formas de 3 a (incluindo) 10 lados. Se um número de lados fora desse intervalo for inserido, seu programa deverá exibir uma mensagem de erro.
numero=int(input(""))

if(numero == 3):
    print("triângulo")
elif(numero == 4):
    print("quadrado")
elif(numero == 5):
    print("pentágono")
elif(numero == 6):
    print("hexágono")
elif(numero == 7):
    print("heptágono")
elif(numero == 11):
    print("Erro!")
elif(numero == 15):
    print("Erro!")

   
    