import somaDoisPontos
from itertools import permutations
import matplotlib.pyplot as plt


#Array que guardará todas as coordenadas do imput
coordMatrix = []



print("Insira as coordenadas do caixeiro. Digite 'exit' para terminar de colocar as coordenadas. \n")

#Loop para inserir as coordenadas
while True:

    coord = input().split()

    #Comando para terminar a interação com o usuário
    if "exit" in coord:
        break

    #Valores adicionados à matriz principal
    coordMatrix.append(coord)








#Lista que armazena a soma das iterações entre os pontos das coordenadas dada a permutação.
#É dado um .clear() quando se coloca outra permutação, já que é outra soma
pontosCalc = []


#Array que vai guardar o resultado de TODAS as permutações e no final, será retirado o menor do array, que é a menor distância que o caixero percorrerá
somasPossiveis = []


#Dicionário que armazena a distância percorrida e as coordenadas em chave e valor respectivamente
somaCoord = {}


#Loop para transformar todos os elementos em inteiros
for i in range(len(coordMatrix)):
    for j in range(2):
        (coordMatrix[i][j]) = int(coordMatrix[i][j])


print(f"Coordenadas: {coordMatrix}")


#coordPermut armazena todas as permutações das coordenadas mas é só permut que consegue percorrer entre as combinações
coordPermut = permutations(coordMatrix)

for permut in (coordPermut):

    for i in range(len(permut) - 1):
        sum = somaDoisPontos.matrixSum(permut[i], permut[i + 1]) #Coloca cada combinação da coordenada e a próxima para ser somado na função que calcula a distância entre doois pontos
        pontosCalc.append(sum) #Depois de calculada, a distância entre somente dois pontos numa lista
    
    #Após o termino de colocar a distância de todos os pontos, é necessário somá-los, para que assim se tenha a distância total do trajeto daquela combinação
    somaCalc = somaDoisPontos.sumFloat(pontosCalc) #Aqui, soma-se todas as coordenadas
    somasPossiveis.append(somaCalc) #E então, armazena-se num array onde terão todas as distâncias de todas as permutações
    
    somaCoord.update({str(somaCalc) : str(permut)}) #Neste dicionário, se guardarâo a coordenada junto com a soma da trajetória
    
    
    pontosCalc.clear() #Aqui, limpa-se o array para que seja possível armazenar a soma das coordenadas de outras combinações

print(f"A menor distancia que o caixeiro pode percorrer dentre as coordenadas {coordMatrix} é {min(somasPossiveis)}")

menorValor = str(min(somasPossiveis))

print(f"Coordenada com a menor distância para o caixeiro: {somaCoord.get(menorValor)}")


#Neste array, pega-se a coordenada da menor distância possível a se percorrer no dicionário 'somaCoord', e transforma a string em uma lista
coordMelhorCaminho = str(somaCoord.get(menorValor)).replace("(","").replace(")","").replace("[","").replace("]","").replace(",", "").split()


#Como ele é armazenado como string, é necessário fazer a conversão para inteiros
coordMelhorCaminho = list(map(int, coordMelhorCaminho))

#Nesta lista, armazena-se as coordenadas para futaramente construir os gráficos
coordPlot = []


count = int(0) #Variável auxiliar para poder acessar os elementos de 'coordMelhorCaminho' e poder indexá-los em um array de 2 dimensões
for index in range((len(coordMelhorCaminho)//2)): #Pelo fato de que quando o array foi construido ele foi colocado em 1D, a intenção é fazer um de 2D, e para isso
                                                  #o novo array terá metade dos indicies do anterior, por isso, //2
    
    #Aqui, pega-se um elemento da lista 1D 'coordMelhorCaminho' e o próximo elemento a fim de colocar os dois elementos NO MESMO ÍNDICE, na lista coordPlot
    coordPlot.append([coordMelhorCaminho[count], coordMelhorCaminho[count + 1]])
    count += 2 #Acrescenta-se 2 à count pois já que pegamos o count e count + 1, para não pegarmos um elemento repetido, precisa-se pegar (count + 1) + 1, ou seja, 2

#Por fim, temos uma lista de 2 dimensões com a melhor coordenada pela qual o Caixeiro pode percorrer

#---------------------------------------------------------------------------------------------Plotagem de Gráficos---------------------------------------------------------------------------------------------

x_plt = []
y_plt = []

for i in range(len(coordPlot)):    
        x_plt.append(coordPlot[i][0])
        y_plt.append(coordPlot[i][1])




ax = plt.plot(x_plt, y_plt, label="Trajetória do caixeiro")
plt.xlim(0, int(max(somasPossiveis)))
plt.ylim(0, int(max(somasPossiveis)))
plt.legend()
plt.show()
