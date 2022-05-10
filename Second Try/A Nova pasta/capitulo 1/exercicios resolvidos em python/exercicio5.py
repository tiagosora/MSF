import math
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats

def main(x1,y1): 
    print()
    print("---------alinea (a)------")
    plt.plot(x1, y1,"o") # coloca os pontos nos graficos (Plot dos pontos x, f(x), MODO = 'ro'=> Apenas os pontos)
    plt.xlabel('L(cm)') # legenda no eixo dos x
    plt.ylabel('X(cm)') # legenda no eixo dos y
    plt.title('Representação dos pontos experimentais') #titulo do grafico
    plt.show() #mostrar grafico
    print()

    print("---------alinea (b)------")
    assert len(x1) == len(y1)
    n=len(x1)
    x=sum(x1)
    y=sum(y1)
    xy=sum(x1[i]*y1[i] for i in range(n))
    xx=sum(x1[i]**2 for i in range(n))
    yy=sum(y1[i]**2 for i in range(n))
    print("somatorio de xy = {:.1f}; somatorio de x = {:.1f}; somatorio de y = {:.1f}; somatorio de xx = {:.1f}; somatorio de yy = {:.2f};". format(xy,x,y,xx,yy))
    print()

    print("---------alinea (c)------")
    m=((n*xy)-(x*y))/((n*xx)-(x**2))
    b=((xx*y)-(x*xy))/((n*xx)-(x**2))
    r=(((n*xy)-(x*y))**2)/(((n*xx)-(x**2))*((n*yy)-(y**2)))
    deltam=abs(m)*math.sqrt(((1/r)-1)/(n-2))
    deltab= deltam* math.sqrt(xx/n)
    print ("m = {:.8f} +/- {:.8f}; b = {:.8f} +/- {:.8f}; r^2 = {:.8f};".format(m,deltam,b, deltab,r))
    print()

    print("---------alinea (d)------")
    #Criação de um array com 10000 valores entre o mínimo e o máximo de x (neste caso é o l)
    #IMPORTANTE: multiplica-se por 0.9 e por 1.1 para que caso haja um valor no mínimo e no máximo da amostra, ele possam ser vistos
    x = np.linspace(np.min(x1)*0.9, np.max(x1)*1.1, 10000)

    lin_reg = stats.linregress(x1, y1) #lista [m,b,r,-,deltam, deltab]
    #plt.plot(x1,y1,"ro",x, x * m + b)
    plt.plot(x, x * lin_reg.slope + lin_reg.intercept)#Plot da funcão (x,f(x))
    plt.plot(x1, y1, "ro")
    plt.title('Representação da reta ') #titulo do grafico
    print()

    print("---------alinea (e)------")
    X=m*165+b
    print("O valor X para L=165.0cm é {:.1f}.\n".format(X))
    #Plot ponto x(165.0) com uma cor diferente
    #IMPORTANTE: Como é só um ponto é preciso colocar o formato 'ro'
    plt.plot(165.0, X ,'ro',color='green')
    plt.show()

x1 = [222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0] 
y1 = [2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0] 
main(x1,y1)

print("---------alinea (f)------")
x2 = [222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0] 
y2 = [2.3,2.2,2.0,2.1,1.6,1.4,1.2,1.0]
main(x2,y2)