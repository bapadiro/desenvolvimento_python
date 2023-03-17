def maximo(lista, ultimoIndice):
    if ultimoIndice == 0:
        return lista[ultimoIndice]
    else:
        valor = maximo(lista, ultimoIndice - 1)
        if valor > lista[ultimoIndice]:
            return valor
        else:
            return lista[ultimoIndice]

vet = [45, 89, 0, 5, 7, 129, 85, 43, 81]
x = maximo(vet, 8)
print(x)