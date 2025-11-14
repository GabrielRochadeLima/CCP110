soma_notas = 0.0
aprovados = 0

for i in range(0, 80):
    while True:
        try:
            nota = float(input(f"Digite a nota do {i}º aluno (0 a 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    soma_notas += nota

    if nota >= 6.0:
        aprovados += 1

media_turma = soma_notas / 80

print("-" * 30)
print(f"Alunos aprovados: {aprovados}")
print(f"Média das notas da turma: {media_turma:.2f}")