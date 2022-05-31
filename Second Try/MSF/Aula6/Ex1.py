# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:14:56 2022

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

vx[0] = v0*np.cos(angle)
vy[0] = v0*np.sin(angle)

ax = 0
ay = g

for i in range(t.size-1):
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



angle1 = 10/180*np.pi
g1 = -9.8
t1 = np.arange(0,3+dt, dt)
y1 = np.zeros(t.size)
x1 = np.zeros(t.size)
vx1 = np.zeros(t.size)
vy1 = np.zeros(t.size)
v01 = 100/3.6

D1 = -g1/(100/3.6)**2

vx1[0] = v0*np.cos(angle)
vy1[0] = v0*np.sin(angle)

#ax = 0
#ay = g

for i in range(t1.size-1):
    v1 = np.sqrt(vx1[i]**2 + vy1[i]**2)
    ax1 = -D1*v1*vx1[i]
    ay1 = g1-D1*v1*vy1[i]
    vx1[i+1] = vx1[i] + ax1 * dt
    vy1[i+1] = vy1[i] + ay1 * dt
    x1[i+1] = x1[i] + vx1[i] * dt
    y1[i+1] = y1[i]+ vy1[i] * dt
    if y1[i+1] < 0:
        break

t1 = t1[:i+2]
x1 = x1[:i+2]
y1 = y1[:i+2]
vx1 = vx1[:i+2]
vy1 = vy1[:i+2]


aux = np.argmin(abs(y[-2:]))
aux1 = np.argmin(abs(y1[-2:]))
tsolosi = t[-2:][aux]
tsolosi1 = t1[-2:][aux1]
xsolosi = x[-2:][aux]
xsolosi1 = x1[-2:][aux1]
print("SEM RES | COM RES")
print("Instante de altura máxima")
print(t[np.where(y == np.amax(y))], " | ", t1[np.where(y1 == np.amax(y1))] )
print("Altura máxima")
print(np.amax(y), " | ", np.amax(y1))
print("Instante de regresso ao solo")
print(tsolosi, " | ", tsolosi1)
print("Maximo alcançe")
print(xsolosi, " | ", xsolosi1)

plt.plot(x,y, label="Sem Res")
plt.plot(x1,y1, label="Com Res")
#plt.plot(t,y,label="ty")
#plt.plot(t,x,label="tx")
plt.legend()
plt.grid()
plt.show()
