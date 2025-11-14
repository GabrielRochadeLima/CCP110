n = int(input("Digite o tamanho: "))

for i in range(n):
    print("$" * i, end="")
    print("@" * (n - i))
