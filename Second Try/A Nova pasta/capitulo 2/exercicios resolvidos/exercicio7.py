import math
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats


def metodoEuler(dt,vinicial,yinicial,ti,tf,vt):
    n=np.int64((tf-ti)/dt) #intervalo de tempo
    t=np.linspace(ti,tf,n) #lista de intervalos de tempo
    print("n: ",n)

    #vetor só com zeros
    vy=np.zeros(n)
    ay=np.zeros(n) 
    y=np.zeros(n)
    
    #alteramos o valor no inicial dos vetores anteriores
    vy[0]=vinicial
    y[0]=yinicial

    D=g/vt**2

    #alterar valores no vetores de acordo com o valor implementado anteriormente
    for i in range(n-1):
        vv=np.abs(vy[i])
        ay[i]=-g-D*vv*vy[i]
        vy[i+1]=vy[i]+ay[i]*dt       
        y[i+1]=y[i]+vy[i]*dt

    #grafico velocidade por 
    plt.plot(t, vy)
    plt.xlabel('t(s)') # legenda no eixo dos x
    plt.ylabel('Vy(m/s)') # legenda no eixo dos y
    plt.show()

    for i in range(n-1):
        if vy[i+1] > 0-0.0005  and  vy[i+1] < 0+0.0005:
            print('altura máxima: ',t[i+1],y[i+1],vy[i+1],vy[i+1]*3600/1000)      
            
    for i in range(n-1):
        if y[i+1] < 0.1  and  y[i+1] > -0.1:
            print('solo: ',t[i+1],y[i+1],vy[i+1],vy[i+1]*3600/1000)    
 
#dados inciais--------
g=9.8 
a=-g #acelerção
vinicial=10 #velocidade incial
yinicial=0 #posiçao inicial
vterminal=100/3.6

#alinea (a)(b) respondida nos apontamentos da aula pratica 5

#alinea (c)
ti=0
tf=4
dt=0.01#incremento do tempo
metodoEuler(dt,vinicial,yinicial,ti,tf,vterminal)
