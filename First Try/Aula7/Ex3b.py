import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym


dt =0.0001

tf = 1.0
ti= 0


x1 = (10*math.pi)/180

n = int((tf-ti)/dt)
T= np.linspace(ti,tf,n)

m = 0.057
v0 = 100/3.6
g = 9.8
ax = 0
ay = -g
v0y = v0*math.sin(x1)
v0x = v0*math.cos(x1)
y0 = 0
x0 = 0



y = np.empty(n)
y[0] = y0

ax_ = np.empty(n-1)
ax_[0] = ax

ay_ = np.empty(n-1)
ay_[0] = ay

vx = np.empty(n)
vx[0] = v0x

vy = np.empty(n)
vy[0] = v0y

x = np.empty(n)
x[0] = x0

vv = np.empty(n)
vv[0] = v0

Em = np.empty(n)


for i in range(n-1):
    vv[i] = np.sqrt((vx[i])*2 + (vy[i]*2))
    
    vy[i+1] = vy[i] + ay*dt
    vx[i+1] = vx[i] + ax*dt
    y[i+1] = y[i] + (vy[i]*dt)
    x[i+1] = x[i] + (vx[i]*dt)
    
    
    Em[i] = m*g*y[i] + 1/2*m*(vv[i])**2

print(Em[0])
print(Em[0.4])
print(Em[0.8])

fig, ax1 = plt.subplots(2)
ax1[0].set_xlabel( 'x (m)' )
ax1[0].set_ylabel( 'y (m)' )

ax1[1].set_xlabel( 'T (s)' )
ax1[1].set_ylabel( 'Em (J)' )
ax1[0].plot(x,y,'-',label='Trajetória da bola')
ax1[1].plot(T,Em,'-',label='Euler sem resistencia')
plt.legend()
plt.show()
