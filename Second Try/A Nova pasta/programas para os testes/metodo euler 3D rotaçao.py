import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy import stats

def maximo(xm1,xm2,xm3,ym1,ym2,ym3):  # máximo pelo polinómio de Lagrange
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xmax=0.5*xmla/(a+b+c)

    xta=xmax-xm1
    xtb=xmax-xm2
    xtc=xmax-xm3

    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xmax, ymax

def zerosv(xm1,xm2,xm3,ym1,ym2,ym3):  # raiz pelo polinómio de Lagrange
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    am=a+b+c
    bm=a*(xm2+xm3)+b*(xm1+xm3)+c*(xm1+xm2)
    cm=a*xm2*xm3+b*xm1*xm3+c*xm1*xm2

    xzero=(bm+np.sqrt(bm*bm-4*am*cm))/(2*am)
    if xm3 > xm1 and (xzero < xm1 or xzero > xm3): 
        xzero=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)


    if xm1 > xm3 and (xzero < xm3 or xzero > xm1):
        xzero=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)

    xta=xzero-xm1
    xtb=xzero-xm2
    xtc=xzero-xm3
    yzero=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xzero, yzero


#dados iniciais
g=9.8
angulo = 10   #!alterar(graus)
ang = np.deg2rad(angulo) #converter para radianos
vinicial = 130/3.6     #!alterar
vterminal= 100/3.6  #!alterar

m=57/1000 #!alterar(g-->KG)
r = 67/2000 #!alterar(mm-->metros)
w=[0,0,0]  #!alterar(rad/s) se nao houver rotaçao [0,0,0]


#valor da aceleração inciais em cada eixo
ay=-g
ax=0
az=0

#valor da velocidades inciais em cada eixo
vx0=vinicial*np.cos(ang)
vy0=vinicial*np.sin(ang)
vz0=0

#valor da posiçoes inciais em cada eixo
x0=-10 #!alterar (posiçao no solo)
y0=1 #!alterar (altura)
z0=0 #!alterar (altura)

tf =2   #!alterar
ti = 0   #!alterar

step= 0.01
n = int((tf - ti) / step)
t=np.linspace(ti,n*step,n)

#-----------calculos analiticos em 2 componentes-
x=x0 + vx0*t + 0.5*ax*t**2
y=y0 + vy0*t + 0.5*ay*t**2
z=z0 + vz0*t + 0.5*az*t**2

vx= vx0 + ax*t
vy= vy0 + ay*t
vz= vz0 + az*t

#vetores zeros....
x_=np.zeros(n)
vx_=np.zeros(n)
ax_=np.zeros(n-1)

y_=np.zeros(n)
vy_=np.zeros(n)
ay_=np.zeros(n-1)

z_=np.zeros(n)
vz_=np.zeros(n)
az_=np.zeros(n-1)

#definir posições iniciais...
x_[0]=x0
vx_[0]=vx0

y_[0]=y0
vy_[0]=vy0

z_[0]=z0
vz_[0]=vz0


A=0.5*np.pi*r**2*1.225*r/m
D= g/vterminal**2
for i in range(n-1):
    v=[vx_[i],vy_[i],vz_[i]]
    fm = A*np.cross(w,v)
    vv=np.sqrt(vx_[i]**2+vy_[i]**2+ vz_[i]**2)

    #eixo dos xx
    ax_[i]=ax-D*vv*vx_[i] + fm[0]
    vx_[i+1]=vx_[i]+ax_[i]*step #!sem resistencia ao ar vx_[i+1]=vx_[i]+ax*step
    x_[i+1] =x_[i]+vx_[i]*step

    #eixo dos yy
    ay_[i]=ay-D*vv*vy_[i]+fm[1]
    vy_[i+1]=vy_[i]+ay_[i]*step #!sem resistencia ao ar vy_[i+1]=vy_[i]+ay*step
    y_[i+1] =y_[i]+vy_[i]*step

     #eixo dos zz
    az_[i]=az-D*vv*vy_[i] +fm[2]
    vz_[i+1]=vz_[i]+az_[i]*step #!sem resistencia ao ar vz_[i+1]=vy_[i]+ay*step
    z_[i+1] =z_[i]+vz_[i]*step
    if i>1 and y_[i-1] < y_[i] and  y_[i+1] < y_[i]  :    # para altura máxima
        print('sucess',i, y_[i-1], y_[i], y_[i+1])
        maxx, maxy=maximo(x_[i-1], x_[i], x_[i+1], y_[i-1], y_[i], y_[i+1])
        print('maximo=',maxx,maxy)
    if i>1 and y_[i-1]*y_[i] < 0 :   # condição de passagem de y positivo para y negativo
        print('sucess solo:',i, t[i], ' alcance = ',x_[i],'solo = ',y_[i])
        zerxx, zeryy=zerosv(x_[i-1], x_[i], x_[i+1], y_[i-1], y_[i], y_[i+1])
        print('alcance =',zerxx,zeryy)


#grafico a 3 dimensoes 
fig = plt.figure().add_subplot(projection='3d')
plt.plot(x_, z_, y_)
plt.show()

#grafico a 2 dimensoes
plt.plot(x_,y_, label='metodo euler')
plt.plot(x,y, label='metodos analiticos')
plt.xlabel('x(m)') 
plt.ylabel('y(m)')
plt.legend()
plt.grid(True)
plt.show()


#----------vetores----
""" a = [0,2,10]
b = [0,1,0]
print(np.dot(a,b))#escalar
print(np.cross(a,b))#vetorial """