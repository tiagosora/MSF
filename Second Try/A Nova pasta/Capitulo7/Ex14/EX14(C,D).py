import matplotlib.pyplot as plt
import numpy as np

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


def main():
    m=1 
    k=1
    wf=1.0
    fo=7.5
    b=0.05
    tf=300
    ti=0

    dt= 0.0001
    n=int((tf-ti)/dt)
    t=np.linspace(ti,n*dt,n)


    x0=-2
    vx0=-4
    ax0=0
    x_=np.empty(n)
    vx_=np.empty(n)
    ax_=np.empty(n-1)
    x_[0]=x0
    vx_[0]=vx0

    maxxtotal=0
    countmax=0
    maxtempos=[]
    tempototal=0

    for i in range(n-1):
        fext=fo*np.cos(wf*t[i])
        fem=-b*vx_[i]
        fx=-k*x_[i]
        Em=fext+fem+fx
        ax_[i]=(fext+fem+fx)/m
        vx_[i+1]=vx_[i]+ax_[i]*dt
        x_[i+1] =x_[i]+vx_[i+1]*dt

        if t[i]>200 and x_[i-1] < x_[i] and  x_[i+1] < x_[i]:
            maxt, maxx=maximo(t[i-1], t[i], t[i+1], x_[i-1], x_[i], x_[i+1])
            maxxtotal +=maxx
            countmax+=1
            maxtempos.append(maxt)

    for i in range(countmax-1):
        tempototal+=maxtempos[i+1]-maxtempos[i]
        
    print("-----------------Alinea (c)-------------------")

    plt.plot(t,x_)
    plt.xlabel('t(s)') 
    plt.ylabel('x(m)')
    plt.grid(True)
    plt.show()

    print("-----------------Alinea (d)-------------------")
    print('A=',maxxtotal/countmax,"T=",tempototal/(countmax-1))




main()