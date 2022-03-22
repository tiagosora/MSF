# Movimento projetil
# Método de Euler

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


dt=0.00001
tf=1.20
n=np.int(tf/dt+0.1)
print('n',n)

def maximo(xm1,xm2,xm3,ym1,ym2,ym3):  # máximo pleo polinómio de Lagrange
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
  
t=np.zeros(n+1)
vy=np.zeros(n+1)
ay=np.zeros(n+1)
y=np.zeros(n+1)
vx=np.zeros(n+1)
ax=np.zeros(n+1)
x=np.zeros(n+1)

g=9.80      # m/s**2                     # INPUT
vt=100*1000/3600  # m/s
vel0=100*1000/3600  # m/s
theta=10*np.pi/180  # rad
v0x=vel0*np.cos(theta)
v0y=vel0*np.sin(theta)
x0=0
y0=0

t[0]=0
vx[0]=v0x
vy[0]=v0y
x[0]=x0
y[0]=y0


tsolo=2*v0y/g     # sem resistência do ar
xsolo=2*v0x*v0y/g
ym=y0+0.5*v0y**2/g
tm=v0y/g
print(' exato sem resist. do ar: tm, ym,tsolo, xsolo =',tm,ym,tsolo,xsolo)