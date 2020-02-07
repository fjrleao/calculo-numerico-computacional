#Implementa o metodo das secantes
#Usado para aproximar a raiz de uma funcao real de uma variavel

#Definindo a funcao
def f(x):
    return (3.0*(x**3) - 2.0*x - 20.0)

#Definindo algoritmo

#Leitura dos dados
x0 = float(input("Entre com x0 (extremo esquerdo do intervalo): "))
x1 = float(input("Entre com x1 (extremo direito do intervalo): "))
erro = float(input("Entre com o erro tolerado: "))

if (f(x0) * f(x1)) < 0:

    #verifica se os chutes ja nao sao as raizes
    if abs(f(x0)) < erro:
        print("Iteracao 0 \nRAIZ = " + str(x0))
    
    elif abs(f(x1)) < erro:
        print("Iteracao 0 \nRAIZ = " + str(x1))
    
    else:
        
        #Variavel contadora
        k = 1

        x2 = x1 - ((f(x1)/(f(x1) - f(x0)))*(x1-x0))        
        
        while (abs(f(x2))) > erro:
            
            x0 = x1
            x1 = x2
            
            x2 = x1 - ((f(x1)/(f(x1) - f(x0)))*(x1-x0)) 
            
            print ("\nIteracao " + str(k) + "\nRAIZ = " + str(x2))
            
            k = k + 1
        
else:
    print("Nao existe raiz no intervalo informado")    
