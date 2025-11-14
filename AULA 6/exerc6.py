contador = 0
soma = 0

while True:
    n = int(input("Digite o numero que deseja: "))
    if (n==0):
        break
    soma+=n
    contador+=1

print(f"Qunatidade de numeros: {contador}.")
print(f"Soma dos números: {soma}")
media = soma/contador
if (contador > 0):
    print(f"A media aritimetica é: {media}")