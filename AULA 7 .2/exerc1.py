
def media (x,y):
    """
    Calcula media entre dois numeros.
    
    """
    res = (x+y)/2
    
    return res

x = float(input("Digite um numero para calcular a media: "))
y = float(input("Digite um numero para calcular a media: "))

print(f"A media é: {media(x,y):.2f}")