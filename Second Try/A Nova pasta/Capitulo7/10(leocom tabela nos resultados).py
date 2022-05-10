import matplotlib.pyplot as plt
import numpy as np


def main(angulo):
    g=9.8
    l=1
    tf=100
    ti=0
    
    dt= 0.01
    n=int((tf-ti)/dt)
    t=np.linspace(ti,n*dt,n)

    ang0=np.deg2rad(angulo)
    w0=0
    aw0=0
    ang_=np.empty(n)
    w_=np.empty(n)
    aw_=np.empty(n-1)
    ang_[0]=ang0
    w_[0]=w0

    maxangtotal=0
    countmax=0
    maxtempos=[]
    tempototal=0

    for i in range(n-1):
        aw_[i]=-g/l*np.sin(ang_[i])
        w_[i+1]=w_[i]+aw_[i]*dt
        ang_[i+1] =ang_[i]+w_[i+1]*dt

        if i>1 and ang_[i-1] < ang_[i] and  ang_[i+1] < ang_[i]:
            maxt, maxang=maximo(t[i-1], t[i], t[i+1], ang_[i-1], ang_[i], ang_[i+1])
            maxangtotal +=maxang
            countmax+=1
            maxtempos.append(maxt)

    for i in range(countmax-1):
        tempototal+=maxtempos[i+1]-maxtempos[i] 
 
    print('ANGULO = {:.8f} A = {:.8f} {:.8f} T = {:.8f} {:.8f}'.format(ang0,maxangtotal/countmax,ang0,tempototal/(countmax-1),2*np.pi*np.sqrt(l/g)))

    #grafico(t,ang_,'t(s)','ang(rad)')


def grafico(x,y,xlabel,ylabel):
    plt.plot(x,y)
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.show()

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


angulos=[1,2,10,15,20,30]

for ang in angulos:
    main(ang)