while True:
    try:
        n = int(input("Digite um número inteiro e positivo:"))
        if n > 0:
            break
        else:
            print("O numero deve ser positivo. Digite novamente")

    except ValueError:
        print("Estrada invalida. Digite um número inteiro.") 


soma = 0

for i in range(1, n + 1):
    soma += 1 / i

print(f"A soma S = 1 + 1/2 + 1/{n} é: {soma:.2f}")
