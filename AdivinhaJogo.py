import random

sorteado = random.randint(1, 1001)
#print(sorteado)

chute = int(input("Tentativa: "))
contador = 1

while chute != sorteado:
    if chute < sorteado:
        print("Tente um número maior")
    elif chute > sorteado:
        print("Tente um número menor")

    chute = int(input("Tentativa: "))
    contador = contador + 1

print("Parabéns você acertou!")
print(contador, " tentativas")
