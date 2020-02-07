import math

#Implementa o metodo da posicao falsa
#Usado para aproximar a raiz de uma funcao real de uma variavel

#Definindo a funcao
def f(x):
    return ((x**3) + x - 1000.0)

def pFalsa (a,b):
    return ((a*f(b))-(b*f(a)))/(f(b)-f(a))
    
#Definindo algoritmo
    
#Leitura dos dados
a = float(input("Entre com a (extremo esquerdo do intervalo): "))
b = float(input("Entre com b (extremo direito do intervalo): "))
erro = float(input("Entre com o erro tolerado: "))

#Variavel contadora
k = 1

#Calculo do ponto x
xanterior = pFalsa(a,b)

if (f(a) * f(xanterior)) < 0:
    b = xanterior
else:
    a = xanterior

xnovo = pFalsa(a,b)

#Condicao para saber se a raiz pertence ao intervalo informado
if (f(a) * f(b)) < 0:
    while abs((xnovo-xanterior)/xnovo):
        #Condicao para troca de ponto e refazer calculo do x 
        if (f(a) * f(xnovo)) < 0:
            b = xnovo
        else:
            a = xnovo

        xanterior = xnovo
        xnovo = pFalsa(a,b)

        print ("Iteracao "+str(k)+ " = "+str(xnovo)) 
        print("a = "+str(a))
        print("b = "+str(b))
        k = k + 1

    print ("RAIZ = "+ str(xnovo))
else:
    print("A raiz nao esta no intervalo informado")