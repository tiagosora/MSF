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
    N = 8
    ## X = ?, Y = ?
    X = np.array([222.0,207.5,194.0,171.5,153,133,113,92])  
    Y = np.array([2.3,2.2,2,1.8,1.6,1.5,1.2,1])

    ## Cálculo dos logaritmos dos pontos experimentais
    log_X = np.array([math.log(x) for x in X])
    log_Y = np.array([math.log(x) for x in Y])

    ## Chamada da função para obter regressão linear
    print("Obtenção de regressão linear utilizando os pontos experimentais iniciais\n")
    m, b = equacao(N,X,Y)  ##em que N é nº pontos experimentais e X e Y os valores a utilizar na regressão linear

    ## Chamada do gráfico com os pontos experimentais iniciais, de modo a averiguar se estes representam um modelo linear
    graph(X,Y,"Regressão Linear","L(cm)","X(cm)") ## Adicionar 2 parâmetros extra com titulos dos eixos

    ## Gráfico da regressão linear com pontos iniciais
    plt.plot(X, m*X + b)

    plt.show()

    ## Alínea e)
    valor = m*165 + b
    print("O valor de X quando L=165.0cm é: {:.2f}".format(valor))

main()