import math

#Implementa o metodo de newton

#Definicao de funcao
def f(x):
    return ((x**3) - x - 1.0)
   
def df(x):
    return (3.0*(x**2) - 1.0)
    
#Definicao do algoritmo
xInicial = float(input("Informe o valor inicial de x: "))
erro = float(input("Informe o erro tolerado: "))

if df(xInicial) != 0:
    x = xInicial - (f(xInicial)/df(xInicial))
    k = 1
    while abs((x-xInicial)/xInicial) >= erro:
        xInicial = x
        print ("Iteracao "+str(k)+ " = "+str(x))
        x = xInicial - (f(xInicial)/df(xInicial))
        k = k + 1
    
    print("A raiz aproximada eh: "+str(x))
else:
    print("Chute inicial invalido!")