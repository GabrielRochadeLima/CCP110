contadores = [0,0,0,0]

while True:
    n = int(input("Digite uma numero ou negativo para sair: "))
    if n < 0:
        break
    if 0 <= n <= 25:
        contadores[0] +=1
    if 26 <=n  <=50:
        contadores[1] +=1    
    if 51 <= n <= 75:
        contadores[2] +=1    
    if 76 <= n <= 100:
        contadores[3] +=1    

print(f"O contadores no intervalor [0 - 25] é: {contadores[0]}")
print(f"O contadores no intervalor [26 - 50] é: {contadores[1]}")
print(f"O contadores no intervalor [51 - 75] é: {contadores[2]}")
print(f"O contadores no intervalor [76 - 100] é: {contadores[3]}")
