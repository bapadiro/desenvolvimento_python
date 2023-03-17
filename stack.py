#pilha é uma lista do Python

def isEmpty(pilha):
    if len(pilha) == 0:
        return True
    else:
        return False

def isFull(pilha):
    return False

def put(pilha, info):
    pilha.append(info)

def pop(pilha):
    return pilha.pop()

def peek(pilha):
    last = len(pilha) - 1
    return pilha[last]
    
                            