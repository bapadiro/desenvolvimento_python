def substitui(frase, letra):

    resposta = ""
    letraUpper = letra.upper()

    for x in frase:
        if x == letra or x == letraUpper:
            resposta = resposta + "*"
        else:
            resposta = resposta + x

    return resposta        


print(substitui("JAbuticaba", "a"))    
