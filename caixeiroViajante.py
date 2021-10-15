import somaDoisPontos
from itertools import permutations
import matplotlib.pyplot as plt

coordMatrix = []



print("Insira as coordenadas do caixeiro. Digite 'exit' para terminar de colocar as coordenadas. \n")

#Loop para inserir as coordenadas
while True:

    coord = input().split()

    if "exit" in coord:
        break

    #Valores adicionados à matriz principal
    coordMatrix.append(coord)








#Lista que armazena a soma das iterações entre os pontos das coordenadas
pontosCalc = []


#Soma de todos os pontos
somasPossiveis = []


#Dicionário que armazena a distância percorrida e as coordenadas
somaCoord = {}


#Loop para transformar todos os elementos em inteiros
for i in range(len(coordMatrix)):
    for j in range(2):
        (coordMatrix[i][j]) = int(coordMatrix[i][j])


print(f"Coordenadas: {coordMatrix}")



coordPermut = permutations(coordMatrix)

for permut in (coordPermut):

    for i in range(len(permut) - 1):
        sum = somaDoisPontos.matrixSum(permut[i], permut[i + 1]) #Coloca as coordenadas corretamentes na função que calcula a distância entre os dois pontos
        pontosCalc.append(sum)#Depois de calculada, coloca essa função na lista
    
    
    somaCalc = somaDoisPontos.sumFloat(pontosCalc)
    somasPossiveis.append(somaCalc)
    
    somaCoord.update({str(somaCalc) : str(permut)})
    
    
    pontosCalc.clear()
    


print(f"A menor distancia que o caixeiro pode percorrer dentre as coordenadas {coordMatrix} é {min(somasPossiveis)}")

maiorValor = str(min(somasPossiveis))

print(f"Coordenada com a menor distância para o caixeiro: {somaCoord.get(maiorValor)}")

coordMelhorCaminho = str(somaCoord.get(maiorValor)).replace("(","").replace(")","").replace("[","").replace("]","").replace(",", "").split()



copyCoordMelhorCaminho = [int(i) for i in coordMelhorCaminho]

coordMelhorCaminho.clear()


count = int(0)
for index in range((len(copyCoordMelhorCaminho)//2) - 1):
        
    coordMelhorCaminho.append([copyCoordMelhorCaminho[count], copyCoordMelhorCaminho[count + 1]])
    count += 2

#---------------------------------------------------------------------------------------------Plotagem de Gráficos#---------------------------------------------------------------------------------------------

x_plt = []
y_plt = []

for i in range(len(coordMelhorCaminho)):    
        x_plt.append(coordMelhorCaminho[i][0])
        y_plt.append(coordMelhorCaminho[i][1])




ax = plt.plot(x_plt, y_plt, label="Trajetória do caixeiro")
plt.xlim(0, int(max(somasPossiveis)))
plt.ylim(0, int(max(somasPossiveis)))
plt.legend()
plt.show()