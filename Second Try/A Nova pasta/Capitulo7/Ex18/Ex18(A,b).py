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
    return xzero, yzero
    
def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf

def main():
    m=1 
    k=1
    wf=1.0
    fo=7.5
    b=0.05
    tf=200
    ti=0
    xeq=0
    alpha= 0.002

    dt= 0.01
    n=int((tf-ti)/dt)
    t=np.linspace(ti,n*dt,n)


    x0=3
    vx0=0
    ax0=0
    x_=np.empty(n)
    vx_=np.empty(n)
    ax_=np.empty(n-1)
    energia=np.empty(n)
    x_[0]=x0
    vx_[0]=vx0

    maxxtotal=0
    countmax=0
    maxtempos=[]
    tempototal=0

    ind = np.transpose([0 for i in range(1000)])

        #15 é um numero arbitario e calculo as 5 primeiras frequencias
    afo=np.zeros(15)
    bfo=np.zeros(15)

    for i in range(n-1):
        fext=fo*np.cos(wf*t[i])
        fem=-b*vx_[i]
        fx=-k*x_[i]*(1+2*alpha*x_[i]**2)
        ax_[i]=(fext+fem+fx)/m
        vx_[i+1]=vx_[i]+ax_[i]*dt
        x_[i+1] =x_[i]+vx_[i+1]*dt
        energia[i]=0.5*k*x_[i]**2*(1+alpha**x_[i]**2) + 0.5*m*vx_[i]

        if t[i]>90 and x_[i-1] < x_[i] and  x_[i+1] < x_[i]:
            maxt, maxx=maximo(t[i-1], t[i], t[i+1], x_[i-1], x_[i], x_[i+1])
            maxxtotal +=maxx
            countmax+=1
            maxtempos.append(maxt)
            ind[countmax]=int(i) #nota que tem de ser inteiro

    t0=ind[countmax-1]
    t1=ind[countmax]

    for i in range(15):
        af, bf = abfourier(t,x_,t0,t1,i)
        afo[i]= af
        bfo[i]= bf
        #print("afo= ", i, af, bf, np.sqrt(af**2 + bf**2))

    li=np.linspace(0,14,15)

    for i in range(countmax-1):
        tempototal+=maxtempos[i+1]-maxtempos[i]
    
    energia[n-1]=0.5*k*x_[n-1]**2*(1+alpha**x_[n-1]**2) + 0.5*m*vx_[n-1]

    print("-----------------Alinea (a)-------------------")

    plt.plot(t,x_)
    plt.xlabel('t(s)') 
    plt.ylabel('x(m)')
    plt.grid(True)
    plt.show()

    print("-----------------Alinea (b)-------------------")
    print('A=',maxxtotal/countmax,"T=",tempototal/(countmax-1))
    

    plt.plot(t,energia)
    plt.xlabel('t(s)') 
    plt.ylabel('e(joule)')
    plt.grid(True)
    plt.show()

    graficoBarras(li,afo,'n','| a_n |')
    graficoBarras(li,bfo,'n','| b_n |')
    a, b = abfourier(t, x_, len(maxtempos) - 2, len(maxtempos) - 1, 2)
    print("a = {}, b = {}".format(a, b))


def graficoBarras(ii,lst,xlabel,ylabel):
    plt.figure()
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.bar(ii,np.abs(lst))
    plt.grid(True)
    plt.show()

main()