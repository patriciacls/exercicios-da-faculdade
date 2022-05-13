'''
    Autor: Patricia Correia de Lima Santos -  Fatec Santana de Parnaíba - Ciência de Dados
    Data: 25_11_2021
    Objetivo: Lista de recursividade do componente curricular Estrutura de dados do
            segundo semestre do curso de ciência de dados.

'''

'''programa 1 : receba 10 números em uma lista e usando recursividade calcule a soma destes números.
'''

numeros = []
for i in range(0,10):
    n = int(input('Digite um numero: '))
    numeros.append(n)
print(f"Lista: {numeros}" )

def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma(lista[1:]) #numero + numeros anteriores
print(f'A soma resulta em=  { soma(numeros)}')


'''
Programa 2: receba um número e o seu expoente, e usando recursividade calcule a potência do número elevado ao expoente.
'''

b = int(input('Digite a base: '))
e = int(input('Digite o expoente: '))
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base*potencia(base,expoente-1)
print(potencia(b,e))

'''Programa 3:  Escreva uma função recursiva para inverter uma lista.'''
lista = []

def inverte(lista):
    if len(lista) == 0:
        return lista
    else:
        return lista[-1:] + inverte(lista[:-1])
lista = inverte([4,5,6,7,8,9])
print(lista)

'''
programa 4: Escreva um programa em para inverter uma string usando recursão.
'''

s= str(input('Insira uma string: '))

def inverte(string):
    if string == '':
        return string 
    else:
        return inverte(string[1:])  + string[0]   
print(inverte(s))

'''
programa 5: Escreve uma função recursiva que , dado um número, faça a contagem regressiva 
(impressa) deste número até 0, imprimindo  "LANÇAR FOGUETE!" ao chegar em zero.
'''
numero = int(input('Quantos segundos para lançamento? '))

def lancamento(num):
    if num == 0:
        print('LANÇAR FOGUETE!')
    else: 
        print(num)
        lancamento(num-1)
lancamento(numero)

