import numpy

#definindo a matriz 
print("Entre com a dimensao do sistema")
n = int(input())
A = numpy.zeros((n,n))
U = numpy.zeros((n,n))
L = numpy.zeros((n,n))
b = numpy.zeros(n)#vetor
y = numpy.zeros(n)#vetor auxiliar y
result = numpy.zeros(n);#vetor resutado final


#ler os valoeres para a matriz de entrada
for i in range(n):#i = linhas
	for j in range(n):#j = colunas
		print("A[%i][%i]: "%(i,j))
		A[i][j] = float(input())
		
#le os valores do vetor b
for i in range(n):
	print("b[%i]: "%i)
	b[i] = float(input())

#criar a matriz L
def matriz_L(mtz):
    for i in range(n):
        mtz[i][i] = 1
        for j in range(n):
            if (mtz[i][j] != 1):
                mtz[i][j] = 0
                
def insere_fm_matrizL(mtz,linha,coluna,m):
    mtz[linha][coluna] = m
    
            
#pega a matriz U
def pega_mtzU(mtz):
    for i in range(n):
        for j in range(n):
            U[i][j] = mtz[i][j] 

#pega o maior pivo
def verificaP(num,mtz):

	maior = abs(mtz[num][num]);
	ml = num
	for i in range(num+1,n):
		if(abs(mtz[i][num]) > maior):
			ml = i
			maior = abs(mtz[i][num])
	#print ("ind:%i"%ml)
	return int(ml)

#faz a troca das linhas
def troca(indice,mtz,indice_ant):
	aux = numpy.zeros(n)
	aux2 = numpy.zeros(n)
	for i in range(n):
		aux[i] = mtz[indice_ant][i]
		mtz[indice_ant][i] = mtz[indice][i]
		mtz[indice][i] = aux[i]
		#atualiza o vertor
		aux2[i] = b[indice_ant]
		b[indice_ant] = b[indice]
		b[indice] = aux2[i]
		
#faz a multiplicacao de L com vetor b para resultar em y
def encontrar_vetor_y(mtz,vetor_y):
    vetor_y[n-n] = b[n-n]/mtz[n-n][n-n]
    for i in range(1,n):
        soma = 0.0
        for j in range(i):
            soma = soma + mtz[i][j]*vetor_y[j]

        vetor_y[i] = (b[i] - soma)/mtz[i][i]
    
#faz a multiplicacao de U com vetor Y para resultar em X
def resutado_final(mtz,y):
    result[n-1] = b[n-1]/mtz[n-1][n-1]
    for i in range(n-2,-1,-1):
        #acumulador
        soma = 0.0
        for j in range(i+1,n):
            soma = soma + mtz[i][j]*result[j]

        result[i] = float((b[i] - soma)/mtz[i][i])


pega_mtzU(A)
#print("mtz A")
#print(A)
matriz_L(L)
print("matriz L semi pronta")
print(L)
for i in range(n-1):#usado para indexa 'pivos'
	v = int(verificaP(i,U))

	if((abs(U[v][i]) > abs(U[i][i])) and v!=i):
		troca (v,U,i)
		'''print(U)
		print("\n")
		print(b)'''
		
	#usado para indexa linhas abaixo do pivo	
	for j in range(i+1,n):#outro meto de usar o range,1 parametro e de onde comeca e o 2 onde termina
		
		M = U[j][i]/U[i][i] #calcula o fator de multiplicacao
		insere_fm_matrizL(L,j,i,M)
		#usado pra indexa a colunas
		for k in range(i,n):
			U[j][k] = U[j][k] - M*U[i][k]
			
		b[j] = b[j] - M*b[i]

print("matriz U:")
print(U)
print("matriz L:")
print(L)
encontrar_vetor_y(L,y)
print("vetor y: ")
print(y)
resutado_final(U,y)
print("resultado final")
print(result)
