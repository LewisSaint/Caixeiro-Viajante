from math import dist, perm
import somaDoisPontos

from itertools import permutations


coordMatrix = []



print("Insira as coordenadas do caixeiro. Digite 'exit' para terminar de colocar as coordenadas. \n")


while True:

    coord = input().split()

    if "exit" in coord:
        break

    coordMatrix.append(coord)






distanciasPossiveis= []


#Processo para transformar todos os elementos em inteiros
for i in range(len(coordMatrix)):
    for j in range(2):
        (coordMatrix[i][j]) = int(coordMatrix[i][j])


print(f"Coordenadas: {coordMatrix}")



coordPermut = permutations(coordMatrix)

for permut in (coordPermut):

    for i in range(len(permut) - 1):
        sum = somaDoisPontos.matrixSum(permut[i], permut[i + 1])
        distanciasPossiveis.append(sum)




print(f"A menor distancia que o caixeiro pode percorrer dentre as coordenadas {coordMatrix} é {min(distanciasPossiveis)}")
