# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:32:22 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.0001
g = 9.8
m = 57/1000
v0 = 100/3.6
ang0 = 10/180*np.pi
t = np.arange(0,15+dt, dt)
    
y0 = 0
x0 = 0
vx0 = v0*np.cos(ang0)
vy0 = v0*np.sin(ang0)

E0 = m*(0.5*v0**2 + g*y0)
 
ind1, ind2 = round(0.4/dt), round(0.8/dt)

x = np.zeros(t.size)
y = np.zeros(t.size)
vx = np.zeros(t.size)
vy = np.zeros(t.size)
v = np.zeros(t.size)
x[0], y[0] = x0, y0
v[0], vx[0], vy[0] = v0, vx0, vy0

for i in range(t.size-1):
    ax = 0
    ay = -g
    vx[i+1] = vx[i] + ax*dt
    vy[i+1] = vy[i] + ay*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    v[i+1] = np.linalg.norm((vx[i+1], vy[i+1]))
    if y[i+1] < 0:
        break;
        
    
t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]
v = v[:i+2]

fig1, ax = plt.subplots(1, 2, figsize=(13,6), layout="constrained")
EM = m*(0.5*v**2 + g*y)

ax[0].plot(x, y)

ax[1].plot(t, EM)
ax[1].set_ylim(E0*0.9, E0*1.1)
plt.show()

print(EM[0])
print(EM[ind1])
print(EM[ind2])
