def isSorted(lista):
    i = 1

    while i < len(lista):
        if lista[i-1] > lista[i]:
            return False
        i = i + 1    

    return True        


v = [2, 6, 9, 10, 3, 12]
resp = isSorted(v)
print(resp)
