import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy import stats

g=9.8
angulo = 10   #alterar(graus)
ang = np.deg2rad(angulo) #converter para radianos
vinicial = 200/3.6     #alterar
vterminal= 6.8  #alterar
D= g/vterminal**2

#valor da aceleração inciais em cada eixo
ay=-g
ax=0

#valor da velocidades inciais em cada eixo
vx0=vinicial*np.cos(ang)
vy0=vinicial*np.sin(ang)

#valor da posiçoes inciais em cada eixo
x0=0 #alterar (posiçao no solo)
y0=1 #alterar (altura)

tf = 1.5   #alterar
ti = 0   #alterar

step= 0.001
n = int((tf - ti) / step)
t=np.linspace(ti,n*step,n)

#vetores zeros....
x_=np.zeros(n)
y_=np.zeros(n)
vx_=np.zeros(n)
vy_=np.zeros(n)
ax_=np.zeros(n-1)
ay_=np.zeros(n-1)

#definir posições iniciais...
x_[0]=x0
y_[0]=y0
vx_[0]=vx0
vy_[0]=vy0

D= g/vterminal**2
for i in range(n-1):
    ax_[i]=ax-D*np.sqrt(vx_[i]**2+vy_[i]**2)*vx_[i]
    ay_[i]=ay-D*np.sqrt(vx_[i]**2+vy_[i]**2)*vy_[i]
    vx_[i+1]=vx_[i]+ax_[i]*step #sem resistencia ao ar vx_[i+1]=vx_[i]+ax*step
    vy_[i+1]=vy_[i]+ay_[i]*step #sem resistencia ao ar vy_[i+1]=vy_[i]+ay*step
    x_[i+1] =x_[i]+vx_[i]*step
    y_[i+1] =y_[i]+vy_[i]*step


plt.title('pena de badminton')
plt.plot(x_,y_, label='com resistencia')
plt.xlabel('x(m)') 
plt.ylabel('y(m)')
plt.legend()
plt.grid(True)
plt.show()


t_0=0
for x in range(n):
    if y_[x]<=0:
        t_0=t[x]
        break

print('tempo de voo: {:.2f}s e x: {:.2f}m. '.format(t_0,x_[int(t_0/step)]))   