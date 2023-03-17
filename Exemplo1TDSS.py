n = int(input("Digite qtd de alunos: "))
i = 0
soma = 0
listaNota = []
while i < n:
    nota = float(input("nota: "))
    soma = soma + nota
    i = i + 1
    listaNota.append(nota)

media = soma / n

print("Média", media)

alunosForamMal = 0
for nota in listaNota:
    if nota < media:
        alunosForamMal = alunosForamMal + 1

print(alunosForamMal," alunos abaixo da média da sala")
print(n - alunosForamMal, " alunos acima da média")
