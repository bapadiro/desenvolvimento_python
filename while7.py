estacoes = ("primavera", "verão", "outono", "inverno")

semana = ("seg", "ter", "qua", "qui", "sex", "sab", "dom")

massa = semana[3]
print(type(massa))
print(massa)

meio = estacoes[1:3]
print(type(meio))
print(meio)


sports = ("judô", "vôlei", "tênis", "bocha", "poker")

print(len(sports))

i = 0

while i < len(sports):
    print(sports[i])
    i = i + 1

