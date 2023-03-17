import Imagem

domino = Imagem.getMatrizImagemCinza("domino.png")

pedra = []
for i in range(34):
    pedra.append([0] * 64)

lin = 14
while lin < (14 + 34):
    col = 15
    while col < (15 + 64):
        pedra[lin - 14][col - 15] = domino[lin][col]
        col = col + 1
    lin = lin + 1

Imagem.salvaImagemCinza("00.png", pedra)





