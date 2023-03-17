#Faça um Jogo de advinhação. Você vai ter 3 chances para descobrir 
# um número sorteado aleatoriamente entre 1 e 10, a cada tentativa 
# o algoritmo informa se o número sorteado é maior ou menor do que 
# o número escolhido.

import random

sorteado = random.randrange(1, 11)
#print(sorteado)

chute = int(input("Chute um numero: "))

#verifica se você acertou ou errou o numero sorteado

acertou = False

if chute > sorteado:
    print("Tente um numero menor")
elif chute < sorteado:
    print("Tente um numero maior")
else:
    print("Parabens, voce acertou")
    acertou = True

if not acertou: #acertou == False
    chute = int(input("Chute um outro numero: "))
    if chute > sorteado:
        print("Tente um numero menor")

    if chute < sorteado:
        print("Tente um numero maior")

    if chute == sorteado:
        print("Parabens, voce acertou")
        acertou = True    








if not acertou:
    chute = int(input("Chute um outro numero: "))
    if chute == sorteado:
        print("Parabens, voce acertou")
    else:
        print("Voce perdeu, o numero era ", sorteado)
    