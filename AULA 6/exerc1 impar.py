ultimo = int(input("Digite o ultimo digito da contagem: "))
x = 0
while x <= ultimo:
    if x % 2 == 1:
        print(x)
    x = x + 1
