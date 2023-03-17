import Imagem

#abrir imagem 
tupla = Imagem.getMatrizImagemColorida('lago_canada.jpg')
matR = tupla[0]
matG = tupla[1]
matB = tupla[2]

#posicao inicial do recorte da imagem
posLin = 50
posCol = 100

largura = 800
altura = 550

print("Colunas ", len(matR[0]))
print("Colunas ", len(matR[0]))

#criar as novas matrizes que vão receber os pixels da imagem original
red = []
green = []
blue = []
lin = posLin
while len(red) < altura:
    linhaR = []
    linhaG = []
    linhaB = []
    col = posCol
    while len(linhaR) < largura:
        linhaR.append(matR[lin][col])
        linhaG.append(matG[lin][col])
        linhaB.append(matB[lin][col])
        col = col + 1
    red.append(linhaR)
    green.append(linhaG)
    blue.append(linhaB)
    lin = lin + 1

Imagem.salvaImagemColorida("lago_canada_tdss.jpg", red, green, blue)