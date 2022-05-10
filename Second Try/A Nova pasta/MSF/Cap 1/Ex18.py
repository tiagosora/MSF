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
    ## X = T (K), Y = E (J)
    X = np.array([200,300,400,500,600,700,800,900,1000,1100])  
    Y = np.array([0.6950,4.363,15.53,38.74,75.08,125.2,257.9,344.1,557.4,690.7])

    ## Cálculo dos logaritmos dos pontos experimentais
    log_X = np.array([math.log(x) for x in X])
    log_Y = np.array([math.log(x) for x in Y])

    ## Chamada da função para obter regressão linear
    print("Obtenção de regressão linear utilizando os pontos experimentais iniciais\n")
    declive, ordenada = equacao(N,X,Y)  ##em que N é nº pontos experimentais e X e Y os valores a utilizar na regressão linear

    ## Chamada do gráfico com os pontos experimentais iniciais, de modo a averiguar se estes representam um modelo linear
    plt.subplot(1,2,1)
    graph(X,Y,"Regressão Linear","T (K)", "E (J)") ## Adicionar 2 parâmetros extra com titulos dos eixos

    ## Gráfico da regressão linear com pontos iniciais
    plt.plot(X, declive*X + ordenada)
    print() 

    ## Gráfico log-log
    plt.subplot(1,2,2)
    graph(log_X, log_Y,"Gráfico log-log","log(T) (K)", "log(E) (J)")
    print("Obtenção de regressão linear usando um modelo log")
    m,b = equacao(N,log_X, log_Y)
    plt.plot(log_X, m*log_X + b)
    print()

    plt.show()

main()