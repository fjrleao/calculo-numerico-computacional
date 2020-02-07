import numpy as np

#Leitura da quantidade de colunas e linhas do vetor
nl = int(input("Numero de linhas da matriz: "))
nc = int(input("Numero de colunas da matriz: "))
	
#Declaracao de matrizes e do vetores
mat = np.zeros((nl,nc))
vet = np.zeros(nl)
vetx = np.zeros(nl)

#Leitura da matriz
for i in range(nl):
	for j in range(nc):
		mat[i][j] = float(input("Mat[" + str(i) + "][" + str(j) + "] = "))

#Leitura do vetor
for i in range(nl):
	vet[i] = float(input("Vet[" + str(i) + "] = "))

print("\nMatriz sem escalonar: ")
print (mat)

print("\nVetor ser escalonar: ")
print(vet)

trocaLinhas = 0
#Escalonamento da matriz e do vetor
for i in range(nl-1): #percorre os pivos
	maior = mat[i][i]
	troca = 'false'

	for l in range(i, nl):
		if (abs(maior) < abs(mat[l][i])):
			maior = mat[l][i]
			posInicial = i
			pos = l
			troca = 'true'

	if (troca == 'true'):
		auxMat = mat[posInicial].copy()
		mat[posInicial] = mat[pos]
		mat[pos] = auxMat
		auxVet = vet[posInicial]
		vet[posInicial] = vet[pos]
		vet[pos] = auxVet
		trocaLinhas += 1

	for j in range(i+1, nl): #percorre linhas
		M = mat[j][i]/mat[i][i]
		vet[j] = vet[j] - (M*vet[i])
		for k in range(i, nl):
			mat[j][k] = mat[j][k] - (M*mat[i][k])

print("\nTroca total de linhas: " + str(trocaLinhas))

print("\nMatriz escalonada: ")
print (mat)

print("\nVetor escalonado: ")
print(vet)


if (mat[nl-1][nl-1] == 0) and (vet[nl-1] == 0):
	print ("\nMultiplas solucoes")

elif (mat[nl-1][nl-1] == 0) and (vet[nl-1] != 0):
	print("\nNao tem solucoes")

else:
	vetx[nl-1] = vet[nl-1]/mat[nl-1][nl-1]

	for i in range(nl-2,-1,-1):
		ac = 0.0
		for j in range(i+1, nl):
			ac = ac + mat[i][j]*vetx[j]
		vetx[i] = (vet[i]-ac)/mat[i][i] 

	print("\nVetor resultado: ")
	print(vetx)