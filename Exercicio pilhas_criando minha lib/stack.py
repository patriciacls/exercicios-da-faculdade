def inicializaPilha():
    p=[]
    return p
#
def pilhaVazia(pilha):
    if len(pilha) > 0:
        return False
    else:
        return True

def pilhaCheia(pilha):
    if len(pilha) >= 1:
        return True
    else:
        return False

def top(pilha):
    return pilha[len(pilha)-1] #ver ultimo elemento
    

def pope(pilha):
    pilha.pop(len(pilha)-1) #retira o elemento

def push (pilha, elemento):#insere um elemento
    pilha.append(elemento)