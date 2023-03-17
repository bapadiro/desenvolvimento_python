def passagem(p, doors):
    for i in range(1, 1001):
        if i % p == 0:
            if doors[i] == True:
                doors[i] = False
            else:
                doors[i] = True
                

portas = [False] * 1001 #boolean[] portas = new boolean[1001];

pes = 1
while pes <= 1000:
    passagem(pes, portas)
    pes = pes + 1

for i in range(1, 1001):
    if portas[i] == True:
        print("Porta aberta: ", i)