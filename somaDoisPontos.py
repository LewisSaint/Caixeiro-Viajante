from math import sqrt


#Soma de dois pontos
def matrixSum(pontoA, pontoB):

    distancia = (            ((pontoB[0] - pontoA[0]) **2 ) + ((pontoB[1] - pontoA[1]) ** 2)           ) #Aplicação da fórmula de distância entre dois pontos
                                                                                                         
                                                                                                        
    distancia = sqrt(distancia)                                                                          #Dado por D = sqrt(Bx - Ax)^2 + ((By - Ay)^2))

    return distancia # Retorna a distância entre os dois pontos dados
    


def sumFloat(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]

    
    return sum