def max (x,y):
    """
    Mostra o maior valor entre dois numeros.
    
    """
    if x > y:
        return x
    else:
        return y
    

x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))

print(f"O maior valor é: {max(x,y)}")