import matplotlib.pyplot as plt
import numpy as np

def main():
    tf=3
    ti=0
    g=9.8
    vt=6.8

    dt= 0.00001
    n=int((tf-ti)/dt)
    t=np.linspace(ti,n*dt,n)

    y0=3
    vy0=0
    y_=np.empty(n)
    vy_=np.empty(n)
    ay_=np.empty(n-1)
    y_[0]=y0
    vy_[0]=vy0

    vy_euler=np.empty(n)
    vy_euler[0]=vy0

    for i in range(n-1):
        y_[i+1],vy_[i+1]=rk4(t[i],y_[i],vy_[i],dt)
        vy_euler[i+1]=vy_euler[i]+(g-g/vt**2*np.abs(vy_euler[i]))*vy_euler[i]*dt

    #grafico(t,vy_,'t','v')

    print("V(runge kutta):{:.6f} |V(euler):{:.6f}".format(vy_[int(2/dt)],vy_euler[int(2/dt)]))

#_______________________________________________________________________________________________________________
def grafico(x,y,xlabel,ylabel):
    plt.plot(x,y)
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

def acelera(t,x,vx):
    g=9.8
    vt=6.8
    return g-g/vt**2*np.abs(vx)*vx

def rk4(t,x,vx,dt):
    ax1=acelera(t,x,vx)
    c1v=ax1*dt
    c1x=vx*dt
    ax2=acelera(t+dt/2.,x+c1x/2.,vx+c1v/2.)
    c2v=ax2*dt
    c2x=(vx+c1v/2.)*dt			# predicto:  vx(t+dt) * dt
    ax3=acelera(t+dt/2.,x+c2x/2.,vx+c2v/2.)
    c3v=ax3*dt
    c3x=(vx+c2v/2.)*dt
    ax4=acelera(t+dt,x+c3x,vx+c3v)
    c4v=ax4*dt
    c4x=(vx+c3v)*dt      
    xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp,vxp

main()