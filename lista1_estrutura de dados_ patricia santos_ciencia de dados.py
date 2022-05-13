'''
Lista 1 - Estrutura de dados
Autor: Patricia C D L Santos
Curso: Ciência de Dados


1.ª) Faça um programa que leia dois valores e informe a média entre eles. (use float como tipo de dado).
'''
print('Exercicio 1: ')
#recebe os valores
n1 = float(input('Insira o primeiro número para calculo da média: '))
n2 = float(input('Insira o segundo número para calculo da média: '))
#calcula a media
media = (n1+n2)/2
#printa a media com format
print(f'A média de {n1} e {n2} é = {media}')
#perfumaria
print('\n')

'''
2.ª) Faça um programa que leia uma temperatura em graus Centígrados e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, onde F é a temperatura em Fahrenheit e C em graus Centígrados
'''
print('Exercicío 2: ')
c=float(input('Quantos Graus Célsius esta fazendo?  '))
#calculo do fahrenheit = (9*celsius/5) + 32
f=(9*c+160)/5
print(f'{c}° Celsius corresponde a {f} fahreinheit')
#perfumaria
print('\n')

'''
3.ª) Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula: VOLUME = 3.14159 * R2 * ALTURA.
'''
print('Exercicio 3: ')
#recebe os valores
raio = float(input('Qual o raio?: '))
raio = raio**2
altura= float(input('Qual a altura?: '))
#calcula aplicando na fórmula
volume = 3.14159*raio*altura
#utilizando format printa o valor
print(f'O volume correspondente de {raio} x {altura} = {volume:3.3f}')
#perfumaria
print('\n')

'''
4.ª) Faça um programa que leia 5 valores e informe o valor do maior.
'''
print('Exercicío 4: ')
n1 = input('Numero1 = ')
maior=n1
n2 = input('Numero 2 = ')
if n2>maior:
    maior=n2
n3 = input('Numero 3 = ')
if n3>maior:
    maior=n3
n4 = input('Numero 4 = ')
if n4>maior:
    maior=n4
n5 = input('Numero 5 = ')
if n5>maior:
    maior=n5
print(f'O maior número é: {maior}')
#perfumaria
print('\n')
'''
5.ª) Solicitar o consumo médio de um veículo, bem como o tempo de viagem e a velocidade média. Com base nestas informações:

 Efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem, utilizando-se um automóvel que faz “x” km/l. 

Para obter o cálculo, o usuário deverá fornecer o tempo gasto na viagem e a velocidade média durante a mesma. 

Desta forma será possível obter a distância percorrida com a fórmula: DISTÂNCIA= TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula: LITROS_USADOS=DISTÂNCIA / “x”. O programa deverá apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.
'''
print('Exercicio 5: ')
consumo_medio = float(input('Quantos litros de combustível seu veículo consome a cada 1 km?'))
tempo = float(input('Quanto tempo sera a viagem em horas? '))
velocidade = float(input('Qual velocidade média das rodovias? '))
distancia = tempo*velocidade
combustivel= distancia*consumo_medio
print(f'Com a velocidade média de {velocidade} percorrida durante {tempo} horas, você percorrerá {distancia} km e consumirá {combustivel} litros de combustível.')