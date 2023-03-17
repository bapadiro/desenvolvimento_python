def intercala(palavra):
    resposta = ""
    i = 0
    while i < len(palavra):
        resposta = resposta + palavra[i] + " "
        i = i + 1
    
    #for c in palavra:
    #    resposta = resposta + c + " "
    return resposta


print(intercala("AUSTRALIA"))