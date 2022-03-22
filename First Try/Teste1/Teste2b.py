import numpy as np
import matplotlib.pyplot as plt
import math



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
  

dt=0.00001
tf=2
n=np.int(tf/dt+0.1)
print('n',n)

g=9.80      # m/s**2                     # INPUT
vt=100*1000/3600  # m/s
vel0=130*1000/3600  # m/s
theta=10*np.pi/180  # rad
v0x=vel0*np.cos(theta)
v0y=vel0*np.sin(theta)
v0z = 0
x0=-10
y0=1
z0=0

t=np.empty(n+1)
vy=np.empty(n+1)
vz = np.empty(n+1)
ay=np.empty(n+1)
az = np.empty(n+1)
y=np.empty(n+1)
vx=np.empty(n+1)
ax=np.empty(n+1)
x=np.empty(n+1)
z = np.empty(n+1)

t[0]=0
vx[0]=v0x
vy[0]=v0y
x[0]=x0
y[0]=y0
vz[0] = 0
z[0] = 0

par=1.225
r=0.067/2
A=0.5*math.pi*r**2*1.225*r
w=100
m=0.057


#tsolo=2*v0y/g     # sem resistência do ar
#xsolo=2*v0x*v0y/g
#ym=y0+0.5*v0y**2/g
#tm=v0y/g
#print(' exato sem resist. do ar: tm, ym,tsolo, xsolo =',tm,ym,tsolo,xsolo)

# d) 
for i in range(n):
    t[i+1]=t[i]+dt
    vel=np.sqrt(vx[i]**2+vy[i]**2)
    dres=g/vt**2
    #ax[i]=0
    #ay[i]=-g     # para teste
    ax[i]=-dres*vel*vx[i]+((A*w*vy[i])/m)
    ay[i]=-g-dres*vel*vy[i]-((A*w*vx[i])/m)
    vx[i+1]=vx[i]+ax[i]*dt  
    vy[i+1]=vy[i]+ay[i]*dt        
    x[i+1]=x[i]+vx[i]*dt  
    y[i+1]=y[i]+vy[i]*dt  
    if i>1 and y[i-1] < y[i] and  y[i+1] < y[i]  :    # para altura máxima
        print('sucess',i, y[i-1], y[i], y[i+1])
        maxx, maxy=maximo(x[i-1], x[i], x[i+1], y[i-1], y[i], y[i+1])
        print('maximo=',maxx,maxy)
    if i>1 and y[i-1]*y[i] < 0 :   # condição de passagem de y positivo para y negativo
        print('sucess solo:',i, t[i], ' alcance = ',x[i],'solo = ',y[i])
        zerxx, zeryy=zerosv(x[i-1], x[i], x[i+1], y[i-1], y[i], y[i+1])
        print('alcance =',zerxx,zeryy)


fig, ax1 = plt.subplots(1)
#ax.set_xticks(np.arange(-5, 20,1))
ax1.set_xlabel( 'x(t) (m)' )
ax1.set_ylabel( 'y(t) (m)' )
ax1.plot(x,y,'-',label='com resistência')
plt.legend()
plt.grid()
ax1.set_title( 'Trajetória de uma bola sem e com resistência do ar  v0=100 km/h, 10º' )
plt.show()
