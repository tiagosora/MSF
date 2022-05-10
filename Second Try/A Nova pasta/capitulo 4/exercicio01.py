import matplotlib.pyplot as plt
import numpy as np
import sympy as sym


#dados iniciais
vi=100/3.6
ang = np.deg2rad(10)
g=9.8
ay=-g
ax=0
vt=100/3.6

x0=0
y0=0
vx0=vi*np.cos(ang)
vy0=vi*np.sin(ang)

tf=1
ti=0
step= 0.01 # delta t
n=int((tf-ti)/step)
t=np.linspace(ti,tf,n)


#calculos analiticos
x=0 + vx0*t+ 0.5*ax*t**2
y=0 + vy0*t+ 0.5*ay*t**2

vx= vx0 + ax*t
vy= vy0 + ay*t



t_= sym.symbols('t',real=True, positive=True)
sol=sym.solve(vy0 + ay*t_)
print('ymax:',0 + vy0*sol[0]+ 0.5*ay*sol[0]**2,'t:',sol[0])

sol=sym.solve(0 + vy0*t_+ 0.5*ay*t_**2)
print('x:',0 + vx0*sol[0]+ 0.5*ax*sol[0]**2,'tempo de voo:',sol[0])


#definir vetores de zeros
x_=np.zeros(n)
y_=np.zeros(n)
vx_=np.zeros(n)
vy_=np.zeros(n)

ax_=np.zeros(n-1)
ay_=np.zeros(n-1)

x_[0]=x0
y_[0]=y0
vx_[0]=vx0
vy_[0]=vy0

D= g/vt**2

for i in range(n-1):
    ax_[i]=ax-D*np.sqrt(vx_[i]**2+vy_[i]**2)*vx_[i]
    ay_[i]=ay-D*np.sqrt(vx_[i]**2+vy_[i]**2)*vy_[i]
    vx_[i+1]=vx_[i]+ax_[i]*step
    vy_[i+1]=vy_[i]+ay_[i]*step
    x_[i+1] =x_[i]+vx_[i]*step
    y_[i+1] =y_[i]+vy_[i]*step

plt.title('pena de badminton')
plt.plot(x,y, label='sem resistencia')
plt.plot(x_,y_, label='com resistencia')
plt.xlabel('x(m)') 
plt.ylabel('y(m)')
plt.legend()
plt.show()