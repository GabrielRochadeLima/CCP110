maior= 0

for x in range (6):
    n = int(input("Digite 6 números positivos: "))
    if n > maior:
        maior = n
print(f"O maior número é: {n}")