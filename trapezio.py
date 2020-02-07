#Algoritmo para fazer integracao numerica usando a regra do trapezio

#define a funcao a ser usada
def f(x):
    return (3*(x*x*x) - 3*x + 1)

#leitura das variaveis
valorInicial = float(input("Informe o valor inicial do intervalo: "))
valorFinal = float(input("Informe o valor final do intervalo: "))    
n = int(input("Informe o numero de subintervalos a ser utilizado: "))

#Calcula h e entao divide por 2
h = (valorFinal - valorInicial)/n
fatorH = h/2

#Inicializa variaveis pra somar os resultados da funcao dentro da formula
soma = 0
fatorFunc = valorInicial + h

#laco que soma as funcoes
for i in range (n-1):
    #print (fatorFunc)
    soma = soma + f(fatorFunc)
    fatorFunc = fatorFunc + h
    
#soma do resultado final    
res = (f(valorInicial) + (2*soma) + f(valorFinal))*fatorH

#mostra o resultado final na tela
print (res)