import matplotlib.pyplot as plt
import numpy as np
import math

def graph(x,y,title, xaxis, yaxis):
    plt.plot(x,y,'o')

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)

def main():
    ## Dados Experimentais
    N = 15
    ## X = Distância Horizontal, Y = Altura da trajetória
    X = np.array([1080,1044,1008,972,936,900,864,828,792,756,720,540,360,180,0])  
    Y1 = np.array([0, 2.25, 5.25, 7.5, 8.75, 12.0, 13.75, 14.75,15.5,17.0,17.5,19.5,18.2,13.0,0])
    Y2 = np.array([0,3.25,6.5,7.75,9.25,12.25,16.0,15.25,16.0,17.0,18.5,20.0,18.5,13.0,0])
    Y3 = np.array([0,4.5,6.5,8.25,9.5,12.5,16.0,15.5,16.6,17.5,18.5,20.25,19.0,13.0,0])
    Y4 = np.array([0,6.5,8.75,9.25,10.5,14.75,16.5,17.5,16.75,19.25,19.0,20.5,19.0,13.0,0])
    
    plt.plot(X,Y1,'o')
    plt.plot(X,Y2,'o')
    plt.plot(X,Y3,'o')
    plt.plot(X,Y4,'o')

    #Gráfico com pontos experimentais
    newX = np.linspace(X[0],X[-1]) 

    plt.subplot(2,2,1)
    plt.plot(X,Y1,'o')
    plt.grid()
    poli1 = np.polyfit(X,Y1,2)
    curva1 = np.poly1d(poli1)
    newY = np.array([curva1(x) for x in newX])
    plt.plot(newX,newY)


    plt.subplot(2,2,2)
    plt.plot(X,Y2,'o')
    plt.grid()
    poli1 = np.polyfit(X,Y2,2)
    curva1 = np.poly1d(poli1)
    newY = np.array([curva1(x) for x in newX])
    plt.plot(newX,newY)


    plt.subplot(2,2,3)
    plt.plot(X,Y3,'o')
    plt.grid()
    poli1 = np.polyfit(X,Y3,2)
    curva1 = np.poly1d(poli1)
    newY = np.array([curva1(x) for x in newX])
    plt.plot(newX,newY)


    plt.subplot(2,2,4)
    plt.plot(X,Y4,'o')
    plt.grid()
    poli1 = np.polyfit(X,Y4,2)
    curva1 = np.poly1d(poli1)
    newY = np.array([curva1(x) for x in newX])
    plt.plot(newX,newY)

    plt.show()
main()