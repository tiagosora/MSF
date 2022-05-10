import math
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats


def metodo(dt,vinicial,yincial,ti,tf,alinea,alinea2,at):
    n=np.int32((tf-ti)/dt) #intervalo de tempo
    t=np.linspace(ti,tf,n) #lista de intervalos de tempo

    #vetor só com zeros
    vy=np.zeros(n) 
    y=np.zeros(n)

    #alteramos o valor no inicial dos vetores anteriores
    vy[0]=vinicial
    y[0]=yinicial

    #alterar valores no vetores de acordo com o valor implementado anteriormente
    for i in range(n-1):
        vy[i+1]= vy[i]-a*dt
        y[i+1]=y[i]+vy[i]*dt

    print("({:s}) Resposta: {:.1f}s".format( alinea,vy[-1]))
    print("({:s}) Resposta: {:.1f}s".format( alinea2,y[int(at/dt)]))

#dados inciais--------
g=9.8 
a=-g #acelerção
vinicial=0 #velocidade incial
yinicial=0 #posiçao inicial

#alinea(a)
print("(a) Resposta: a acelraçao corresponde a derivada da equaçao da velocidade (a(t)=dv/dt)")

tinicial=0 #tempo inicial
tfinal=3.0 #tempo final

#alinea(b/e)
dt=0.01 #incremento temporal 
metodo(dt,vinicial,yinicial,tinicial,tfinal,"b","e",2)


#alinea (c/f)
dt=0.001 #incremento temporal 
metodo(dt,vinicial,yinicial,tinicial,tfinal,"c","f",2)

#alinea(d)
#analiticamente v= v0+ a*t
v3y=vinicial+ g*3 #velocidade instanea no instante 3 (eq. das velocidades) 
print("(d) Resposta: Valor exato em Vx(3s): {:.1f}s".format( v3y))
#Resposta:Os valores dão todos os mesmo.



#alinea(g)
#analiticamente y= y0+v0*t+ 1/2*a*t**2
tf=2
y2=1/2*g*tf**2
print("(g) Resposta: Valor exato em x(2s):",y2,"m.")
#Resposta: Quando o passo diminui o valor aproximado aproxima-se do valor exato.




