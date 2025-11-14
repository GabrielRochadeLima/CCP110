L = int(input("Digite um número de linhas: "))
C = int(input("Digite o número de colunas: "))

for i in range(L):
    for j in range(C):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()
