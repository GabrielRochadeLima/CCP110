# Desenvolva um algoritmo que pergunte ao usuário se ele deseja calcular o volume do Dodecaedro (12 faces) ou do Icosaedro (20 faces) regular. Para realizar o cálculo, receba do usuário o valor da aresta a.

# Dodecaedro:

 
# V=15+75–√4a3


# Icosaedro:

 
# V=512(3+5–√)a3


# Por exemplo:

# Input	Resultado
# dodecaedro
# 1
# Você deseja calcular o volume do dodecaedro ou icosaedro: dodecaedro
# Digite o valor da aresta a em metros: 1
# O volume de um dodecaedro regular com 1.00 de aresta é: 7.66
# icosaedro
# 1
# Você deseja calcular o volume do dodecaedro ou icosaedro: icosaedro
# Digite o valor da aresta a em metros: 1
# O volume de um icosaedro regular com 1.00 de aresta é: 2.18
# dodecaedro
# 3
# Você deseja calcular o volume do dodecaedro ou icosaedro: dodecaedro
# Digite o valor da aresta a em metros: 3
# O volume de um dodecaedro regular com 3.00 de aresta é: 206.90

from math import *

forma=(input("Você deseja calcular o volume do dodecaedro ou icosaedro: "))
a=float(input("Digite o valor da aresta a em metros: "))

if(forma=="dodecaedro"):
    v = ((15+7*sqrt(5))/4)*(a**3)
else:
    v = 5/12*(3+sqrt(5))*(a**3)
    
print(f"O volume de um {forma} regular com {a:.2f} de aresta é: {v:.2f}")