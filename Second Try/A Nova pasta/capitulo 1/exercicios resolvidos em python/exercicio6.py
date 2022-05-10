import matplotlib.pyplot as plt 
import numpy as np
import math 


def main(): 
    #Aqui foi usada a função `linspace` para gerar o array de tempo automaticamente
    t = np.linspace(0, 9, 10)
    d=[0.00, 0.735, 1.363, 1.739, 2.805, 3.814,4.458,4.355,5.666,5.329]
    
    print("---------alinea (a)------")
    plt.plot(t, d,"o") # coloca os pontos nos graficos
    plt.xlabel('t(min)') # legenda no eixo dos x
    plt.ylabel('d(km)') # legenda no eixo dos y
    plt.title('Representação dos pontos experimentais') #titulo do grafico
    plt.show() #mostrar grafico 
    print()
    # RESPOSTA: Localmente nao é constante, mas podemos considerar uma relação entre o tempo e a distancia percorrida linear se nao formos minuciosos

    print("---------alinea (b)------")
    assert len(t)== len(t)
    n=len(t)
    x=sum(t)
    y=sum(d)
    xy=sum(t[i]*d[i] for i in range(n))
    xx=sum(t[i]**2 for i in range(n))
    yy=sum(d[i]**2 for i in range(n))
    m=((n*xy)-(x*y))/((n*xx)-(x**2))
    b=((xx*y)-(x*xy))/((n*xx)-(x**2))
    r=(((n*xy)-(x*y))**2)/(((n*xx)-(x**2))*((n*yy)-(y**2)))
    deltam=abs(m)*math.sqrt(((1/r)-1)/(n-2))
    deltab= deltam* math.sqrt(xx/n)
    print ("m = {:.2f} +/- {:.2f}; b = {:.2f} +/- {:.2f}; r^2 = {:.3f};".format(m,deltam,b, deltab,r))
    print()

    print("---------alinea (c)------")
    print("A velocidade média do ciclista é {:.2f}.". format(m))
    print()

    print("---------alinea (d)------")
    c1=np.polyfit (t,d,1)
    print(c1)
    M=c1[0] #declive (velocidade em Km/min)
    B=c1[1] #ordenada na origem 
    print()
    
    print("---------alinea (e)------")
    v= M*60
    print("velocidade é {:.0f}km/h".format(v))
    print()
    
    #NOTA: Não pede para dar plot da reta, mas vou fazer à mesma
    plt.plot(t, d,"o") 
    plt.plot(t,t*m+b)
    plt.show()

main()