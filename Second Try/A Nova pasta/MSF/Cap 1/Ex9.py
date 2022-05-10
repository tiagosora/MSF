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
    ## X = ?, Y = ?
    X = np.array([0,5,10,15,20,25,30,35,40,45])  
    Y = np.array([9.676,6.355,4.261,2.729,1.862,1.184,0.768,0.4883,0.3461,0.2119])

    ## Cálculo dos logaritmos dos pontos experimentais
    log_Y = np.array([math.log(x) for x in Y])

    ## Chamada da função para obter regressão linear
    print("Obtenção de regressão linear utilizando os pontos experimentais iniciais\n")
    declive, ordenada = equacao(N,X,Y)  ##em que N é nº pontos experimentais e X e Y os valores a utilizar na regressão linear

    ## Chamada do gráfico com os pontos experimentais iniciais, de modo a averiguar se estes representam um modelo linear
    plt.subplot(1,2,1)
    graph(X,Y,"Regressão Linear","T (dias)", "Atividade (mCi)") ## Adicionar 2 parâmetros extra com titulos dos eixos

    ## Gráfico da regressão linear com pontos iniciais
    plt.plot(X, declive*X + ordenada)

    ## Caso seja necessário adaptar o modelo a gráficos log ou semilog, chamar novo gráfico com pontos
    ## experimentais adaptados, e fazer plot da equação obtida. Gráficos podem ser obtidos com recurso a plt.plot()
    ## Fazer plt.subplot e/ou plt.figure caso facilitie visualizaçao. plt.subplot(nº linhas, nº colunas, posição do gráfico)
    plt.subplot(1,2,2)
    graph(X,log_Y,"Modelo semilog","T (dias)", "log(Atividade) (mCi)")
    print("Obtenção de regressão linear usando um modelo semilog")
    declive, ordenada = equacao(N,X,log_Y) 
    plt.plot(X, declive*X + ordenada)


    ## Não esquecer que:
    ## Gráfico log/log -> Lei de Potência -> y = c*x^n
    ## Gráfico semilog (logy) -> Lei Exponencial -> y = y0 * e^alfa*x
    ## Responder a questões extra que o exercicio proponha, antes de mostrar os gráficos


    plt.show()

main()