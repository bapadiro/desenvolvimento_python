minhasStrings = []

contador = 0
while contador < 10:
    texto = input("Digite texto: ")
    minhasStrings.append(texto)
    contador = contador + 1

i = len(minhasStrings) - 1    
while i >= 0:
    print(minhasStrings[i])
    i = i - 1
