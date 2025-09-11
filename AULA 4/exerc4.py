salario = float(input("Digite seu salario: "))

if(salario > 1250):
    aumento= (0.15 * 1250 + 0.10 * (salario - 1250))    
else:
    aumento = (salario*0.15) 
    
salario_novo = salario + aumento
print(f"Novo salario :{salario_novo :.2f} - aumento {aumento}")
        