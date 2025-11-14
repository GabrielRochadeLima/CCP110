L = int(input("Digite um numero de linhas: "))
C = int(input("Digite o nuemro de colunas: "))

for i in range(L):
    for j in range(C):
        if L == 0 and L == L-1 or C == 0 or C == C -1:
            print("*", end=" ")
        else:
            print("*", end=" ")
    print()
