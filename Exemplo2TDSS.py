def descobreMaiorMenor(lista):
    maior = lista[0]      #estabeleci base de comparacao
    menor = lista[0]      #entre os valores da lista
    i = 1
    while i < len(lista):
        if maior < lista[i]:  #verificando se há algum valor
            maior = lista[i]  #maior do que o atual

        if menor > lista[i]:
            menor = lista[i]
        i = i + 1    

    return (menor, maior)

conjunto = [3, -6, 18, 25, 9, -10, 5]
resultado = descobreMaiorMenor(conjunto)
print(resultado)
