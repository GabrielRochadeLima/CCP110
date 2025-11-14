def multiplo (x,y):
    """
    Mostra se x é multuplo de y
    
    """
    return x % y == 0
 
x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))

if multiplo (x,y):
    print(f"{x} é multiplo de {y}")
else:
    print(f"{x} não é multiplo de {y}")