import matplotlib.pyplot as plt
import numpy as np

def main(alinea, x):
    l=1  #!comprimento da corda
    g=9.8
    tf=100
    ti=0

    dt= 0.01
    n=int((tf-ti)/dt)
    t=np.linspace(ti,n*dt,n)

    #valores inciais
    ang0=np.deg2rad(x)
    w0=0
    aw0=0

    #inicializaçao dos vetores
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
        
    print("-----------------Alinea {} -------------------".format(alinea))
    plt.plot(t,ang_)
    plt.xlabel('t(s)') 
    plt.ylabel('angulo(rad)')
    plt.show()

    print('A=',maxangtotal/countmax,"T=",tempototal/(countmax-1))


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

main("a",1)
main("b",5)
main("c",10)
main("d",15)
main("e",20)
main("f",30)