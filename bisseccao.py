#Implementa o metodo da bisseccaoo
#Usado para aproximar a raiz de uma funcao real de uma variavel

#Definindoa a funcao
def f(x):
    return ((x**3) - x - 1.0)

#Definindo algoritmo
a = float(input("Entre com a (extremo esquerdo do intervalo): "))
b = float(input("Entre com b (extremo direito do intervalo): "))
erro = float(input("Entre com o erro tolerado: "))

k = 1
while ((b-a) > erro):
    x = (a+b)/2.0
    print ("Iteracao "+str(k)+ " = "+str(x))
    fX = f(x)
    fA = f(a)
    if (fA*fX) < 0:
        b = x
    elif(fA*fX) > 0:
        a = x
    else:
        break
    
    k = k + 1
    
print ("RAIZ = "+ str((a+b)/2.0))