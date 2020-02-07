import numpy as np

#Algoritmo para integracao numerica usando regra de 1/3 de simpson

#define a funcao a ser usada
def f(x):
    return (3*(x*x*x) + x)
    
#leitura das variaveis
valorInicial = float(input("Informe o valor inicial do intervalo: "))
valorFinal = float(input("Informe o valor final do intervalo: "))    
n = int(input("Informe o numero de subintervalos a ser utilizado: "))

#Calcula h e entao divide por 3
h = (valorFinal - valorInicial)/n
fatorH = h/3

#Calcula parametro que sera usado na funcao
fator2 = valorInicial + (2*h)
fator4 = valorInicial + h
calcFator2 = 0
calcFator4 = 0

for i in np.arange(fator4, valorFinal, (h*2)):
    #print("Fator4: " + str(fator4))
    calcFator4 = calcFator4 + f(fator4)
    fator4 = fator4 + (h*2)
    
for i in np.arange(fator2, valorFinal, (h*2)):
    #print("Fator2: " + str(fator2))
    calcFator2 = calcFator2 + f(fator2)
    fator2 = fator2 + (h*2)
    
calcFator2 = calcFator2 * 2
calcFator4 = calcFator4 * 4

res = (f(valorInicial) + calcFator4 + calcFator2 + f(valorFinal))*fatorH

print (res)