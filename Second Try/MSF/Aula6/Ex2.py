# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:40:59 2022

@author: draki
"""
import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
angle = 10/180*np.pi
g = -9.8
t = np.arange(0,3+dt, dt)
y = np.zeros(t.size)
x = np.zeros(t.size)
vx = np.zeros(t.size)
vy = np.zeros(t.size)
v0 = 100/3.6

D = -g/(100/3.6)**2

vx[0] = v0*np.cos(angle)
vy[0] = v0*np.sin(angle)

#ax = 0
#ay = g

for i in range(t.size-1):
    v = np.sqrt(vx[i]**2 + vy[i]**2)
    ax = -D*v*vx[i]
    ay = g-D*v*vy[i]
    vx[i+1] = vx[i] + ax * dt
    vy[i+1] = vy[i] + ay * dt
    x[i+1] = x[i] + vx[i] * dt
    y[i+1] = y[i]+ vy[i] * dt
    if y[i+1] < 0:
        break

t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]

print("Instante de altura máxima")
print(t[np.where(y == np.amax(y))])
print("Altura máxima")
print(np.amax(y))
print("Instante de regresso ao solo")
print(t[i-1])
print("Maximo alcançe")
print(x[i-1])


#splt.plot(x,y,label="yx")
plt.plot(t,y,label="ty")
plt.plot(t,x,label="tx")
plt.legend()
plt.show()
