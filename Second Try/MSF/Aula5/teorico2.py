# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:39:43 2022

@author: draki
"""
import matplotlib.pyplot as plt
import numpy as np

g = -9.8
dt = 0.0001
t = np.arange(0,1+dt, dt)
y = np.zeros(t.size)

vy = np.zeros(t.size)

vx = np.zeros(t.size)

x = np.zeros(t.size)
vy[0] = 4.82
vx[0] = 27.36
ax = 0    

        
for i in range(0, t.size-1):
        vy[i+1] = vy[i] + g*dt # velocidade no instante
        y[i+1] = y[i] + vy[i] * dt
        vx[i+1] = vx[i] + ax * dt
        x[i+1] = x[i] + vx[i] * dt
        
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.plot(x, y, label="pos")

plt.legend()
