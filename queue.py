from typing import final


def InicFila():
    fila = list()
    return fila

def filaVazia(fila):
    if len(fila) < 0 :
        return "Fila vazia"

def filaCheia(fila):
    if len(fila) > 0:
        return 'Fila Cheia'

def Enqueue(fila,elemento):
    fila.append(elemento)

def Dequeue():
    fila.pop(0)

    

