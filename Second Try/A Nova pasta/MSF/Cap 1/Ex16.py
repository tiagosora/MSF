import matplotlib.pyplot as plt
import numpy as np
import math

# Função utilizada para obter gráficos simples
def graph(x,y,title = "Gráfico", xaxis = "Eixo X", yaxis = "Eixo Y"):
    plt.plot(x,y,'o')

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)

# Função utilizada para obter as equações das regressões lineares
# Aplicando o Metodo dos Minimos Quadráticos

def equacao(N,X,Y):
    ## Cálculo dos somatórios para as fórmulas
    sumX = sum(X)
    sumY = sum(Y)
    sumXsquared = sum([x**2 for x in X])
    sumYsquared = sum([x**2 for x in Y])

    ## Somatório x*y
    sumXY = 0
    for i in range(0,N):
        sumXY += X[i]*Y[i]

    ##Resultados dos Somatórios
    print("O resultado de sumX é: {:.1f}".format(sumX))
    print("O resultado de sumY é: {:.1f}".format(sumY))
    print("O resultado de sumXsquared é: {:.1f}".format(sumXsquared))
    print("O resultado de sumYsquared é: {:.1f}".format(sumYsquared))
    print("O resultado de sumXY é: {:.1f}".format(sumXY))

    # Cálculo do declive, ordenada na origem e R
    declive = (N*sumXY - sumX*sumY)/(N*sumXsquared - sumX**2)
    ordenada = (sumXsquared*sumY - sumX*sumXY)/(N*sumXsquared - sumX**2)
    R = (N*sumXY- sumX*sumY)**2/((N*sumXsquared - (sumX)**2)*(N*sumYsquared - sumY**2))

    # Cálculo dos Erros
    erroDeclive = abs(declive)*math.sqrt(((1/R)-1)/(N-2))
    erroOrdenada = erroDeclive*math.sqrt(sumXsquared/N)

    #Resultados do declive, ordenada na origem e R
    print()
    print("O declive obtido é: {:.8f}".format(declive))
    print("A ordenada na origem é: {:.8f}".format(ordenada))
    print("O valor do R é: {:.8f}".format(R))
    print("O erro do declive é: {:.4f}".format(erroDeclive))
    print("O erro da ordenada é: {:.4f}".format(erroOrdenada))

    print()
    print("Logo, o valor do declive é {:.6f} +- {:.2f} km/minuto.".format(declive,erroDeclive))
    print("O valor da ordenada na origem é {:.6f} +- {:.2f} km.".format(ordenada,erroOrdenada))

    return declive, ordenada

def main():
    ## Dados Experimentais
    N = 10
    ## X = tempo (min), Y = dist (km)
    X = np.array([0,1,2,3,4,5,6,7,8,9])  
    Y = np.array([0.00,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329])

    ## Chamada da função para obter regressão linear
    print("Obtenção de regressão linear utilizando os pontos experimentais iniciais\n")
    declive, ordenada = equacao(N,X,Y)  ##em que N é nº pontos experimentais e X e Y os valores a utilizar na regressão linear

    ## Chamada do gráfico com os pontos experimentais iniciais, de modo a averiguar se estes representam um modelo linear
    graph(X,Y,"Regressão Linear","Tempo (min)","Distância (km)") ## Adicionar 2 parâmetros extra com titulos dos eixos

    ## Gráfico da regressão linear com pontos iniciais
    plt.plot(X, declive*X + ordenada, label="Curva Original")
    print() ##Descrever a conclusão obtida ao analisar a regressão linear

    ## Alínea d)
    ply = np.polyfit(X,Y,1)
    poly = np.poly1d(ply)

    newX = np.linspace(X[0], X[-1],10)
    newY = np.array([poly(x) for x in newX])

    ## Regressão Linear com Polyfir
    print("Obtenção de regressão linear utilizando o polyfit\n")
    declive, ordenada = equacao(N,newX,newY)  ##em que N é nº pontos experimentais e X e Y os valores a utilizar na regressão linear


    plt.plot(newX, newY, label="Polyfit")
    plt.show()


main()