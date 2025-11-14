# Inicializa as variáveis
soma_idade = 0
total_pessoas = 0
soma_salario_homens = 0
total_homens = 0
mulheres_salario_baixo = 0

while True:
    try:
        idade = int(input("Digite a idade (ou um valor negativo para encerrar): "))

        if idade < 0:
            break

        sexo = input("Digite o sexo (M/F): ").upper()
        salario = float(input("Digite o salário: "))

        # a) Média de idade do grupo
        soma_idade += idade
        total_pessoas += 1

        if sexo == 'M':
            # b) Média de salários dos homens
            soma_salario_homens += salario
            total_homens += 1
        elif sexo == 'F':
            # c) Quantidade de mulheres com salário abaixo de R$600,00
            if salario < 600.00:
                mulheres_salario_baixo += 1
    
    except ValueError:
        print("Entrada inválida. Digite os dados corretamente.")
        continue

# Calcula as médias (evita divisão por zero)
media_idade = soma_idade / total_pessoas if total_pessoas > 0 else 0
media_salario_homens = soma_salario_homens / total_homens if total_homens > 0 else 0

# Exibe os resultados
print("\n--- Resultados da pesquisa ---")
print(f"a) Média de idade do grupo: {media_idade:.2f} anos")
print(f"b) Média de salários dos homens: R$ {media_salario_homens:.2f}")
print(f"c) Quantidade de mulheres com salário abaixo de R$600,00: {mulheres_salario_baixo}")