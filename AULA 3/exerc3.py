valor_horat = float(input("Digite o valor da hora trabalhada: "))
hora_trabalho = float(input("Digite as horas trabalhadas no mês: "))

salario_bruto = valor_horat*hora_trabalho
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05

salario_liquido = salario_bruto - ir - inss - sindicato


print(f"+ Salário bruto: R$ {salario_bruto:.2f}")
print(f"- IR (11%): R$ {ir:.2f}")
print(f"- INSS (8%): R$ {inss:.2f}")
print(f"- Sindicato (5%): R$ {sindicato:.2f}")
print(f"Seu salário líquido é de: R$ {salario_liquido:.2f}")