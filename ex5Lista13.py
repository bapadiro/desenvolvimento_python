import stack

def haCasamento():
    #exercicio
    
def validaSequencia(sequencia):
    pilha = []
    for c in sequencia:
        if c == '(' or c == '[' or c == '{':
            stack.put(pilha, c) #empilhando c
        else:
            if stack.isEmpty(pilha):
                print("faltou elementos na pilha")
                return False
            a = stack.pop(pilha)
            if not haCasamento(a, c):
                print("Nao houve match entre os caracteres")
                return False

    if stack.isEmpty(pilha):
        return True
    else:
        print("Sobrou caracter de abertura na sequencia")
        return False    


s = '[[{}()([])]]'
resp = validaSequencia(s)
if resp:
    print(s, "é bem formada")
else:
    print(s, "não é bem formada")    
