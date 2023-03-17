n = int(input("Digite n: "))
i = 0
v = []
while i < n:
    num = float("Informe número real: ")
    v.append(num)
    i = i + 1

i = 0
j = n - 1
while i <= j:
    print(v[i] + v[j])
    i = i + 1
    j = j - 1

