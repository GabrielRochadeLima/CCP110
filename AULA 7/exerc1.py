num = int(input("Digite  a quantidade de numeros a serem testados: "))
num_primos = 0
for i in range(num):
    numero = int(input("Digite  numeros inteiros: "))
    eh_primo = True


    for i in range(2,numero):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo and numero > 1:
        num_primos+=1

print(f"Foram digitados {num_primos} numero primos")

