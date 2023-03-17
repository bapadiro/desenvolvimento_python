def intercala(a, b):
    resp = []
    i = 0
    j = 0 
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            resp.append(a[i])
            i = i + 1
        else:
            resp.append(b[j])
            j = j + 1

    while j < len(b):
        resp.append(b[j])
        j = j + 1            

    while i < len(a):
        resp.append(a[i])
        i = i + 1

    return resp        