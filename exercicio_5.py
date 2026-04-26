aluno = input("Nome do aluno: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

# Calculando a média
media = (n1 + n2 + n3) / 3

print("=" * 30)
print(f"       BOLETIM ESCOLAR")
print("=" * 30)
print(f"Aluno: {aluno}")
print(f"Média: {media:.1f}")

# Lógica de aprovação
if media >= 7.0:
    print("Situação: APROVADO(A)")
else:
    print("Situação: REPROVADO(A)")
print("=" * 30)