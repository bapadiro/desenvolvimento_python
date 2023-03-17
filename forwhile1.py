import stack

frase = "ontem choveu mas hoje fez sol"
fraseInvertida = ""
pilha = []

for c in frase:
    if c != ' ':
        stack.put(pilha, c)
    else:
        while not stack.isEmpty(pilha):
            fraseInvertida = fraseInvertida + stack.pop(pilha)
        fraseInvertida = fraseInvertida + c


while not stack.isEmpty(pilha):
    fraseInvertida = fraseInvertida + stack.pop(pilha)

print(fraseInvertida)

