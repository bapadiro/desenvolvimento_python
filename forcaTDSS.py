def criaTabuleiro(pal):
    resposta = ""
    for c in pal:
        resposta = resposta + "_" + " "
    return resposta

def atualizaTabuleiro(pal, letras):
    resp = ""
    for c in pal:
        if c in letras:
            resp = resp + c + " "
        else:
            resp = resp + "_ "
    return resp            

erros = 0
acertou = False
palavra = "Africa do Sul"
letrasChutadas = ""

palavraOculta = criaTabuleiro(palavra)

while erros < 4 and not acertou:
    print(palavraOculta)
    print("Erros: ", erros)
    letra = input("Letra: ")

    letrasChutadas = letrasChutadas + letra

    if letra in palavra:
        palavraOculta = atualizaTabuleiro(palavra, letrasChutadas)
    else:
        erros = erros + 1    
    
    if not "_" in palavraOculta:
        acertou = True  
