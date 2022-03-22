import numpy as np
import matplotlib.pyplot as plt
import math
  
dt=0.00001
tf=2
n=np.int(tf/dt+0.1)
print('n',n)

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
Em = np.zeros(n+1)



g=9.80      # m/s**2                     # INPUT
vt=100*1000/3600  # m/s
vel0=100*1000/3600  # m/s
theta=10*np.pi/180  # rad
v0x=vel0*np.cos(theta)
v0y=vel0*np.sin(theta)
x0=-10
y0=1

t=np.empty(n+1)
vy=np.empty(n+1)
ay=np.empty(n+1)
y=np.empty(n+1)
vx=np.empty(n+1)
ax=np.empty(n+1)
x=np.empty(n+1)
Em = np.empty(n+1)

t[0]=0
vx[0]=v0x
vy[0]=v0y
x[0]=x0
y[0]=y0

par=1.225
r=0.067/2
A=0.5*math.pi*r**2*1.225*r
w=100
m=0.057

 
for i in range(n):
    t[i+1]=t[i]+dt
    vel=np.sqrt(vx[i]**2+vy[i]**2)
    dres=g/vt**2
    ax[i]=-dres*vel*vx[i]-((A*w*vy[i])/m)
    ay[i]=-g-dres*vel*vy[i]+((A*w*vx[i])/m)
    vx[i+1]=vx[i]+ax[i]*dt  
    vy[i+1]=vy[i]+ay[i]*dt        
    x[i+1]=x[i]+vx[i]*dt  
    y[i+1]=y[i]+vy[i]*dt 

    Em[i] = m*g*y[i] + 1/2*m*(vel[i])**2 

    if t[i] == 0.4:
        print(t[i] + ": " + Em[i])
    if t[i] == 0.8:
        print(t[i] + ": " + Em[i])
    


fig, ax1 = plt.subplots(2)
ax1[0].set_xlabel( 'x (m)' )
ax1[0].set_ylabel( 'y (m)' )

ax1[1].set_xlabel( 'T (s)' )
ax1[1].set_ylabel( 'Em (J)' )
ax1[0].plot(x,y,'-',label='Trajetória da bola')
ax1[1].plot(T,Em,'-',label='Euler com resistencia')
plt.legend()
plt.show()
