# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:29:46 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.01

t = np.arange(0,500+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

Cyu = 0.004
Cres = 0.9
area = 0.3
Par = 1.225
m = 75
Potencia = 298.28
vx[0] = 1
g = 9.8

for i in range(t.size-1):
    Fcic = Potencia/vx[i]
    FRes = Cres/2*area*Par*vx[i]**2+Cyu*m*g + m*g*np.sin((5*np.pi)/180) +  Cyu*m*g*np.cos((5*np.pi)/180)
    F = Fcic - FRes
    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    if(x[i] >= 2000):
        break;
        
        
        
t = t[:i+1]
x = x[:i+1]
ax = ax[:i+1]
vx = vx[:i+1]

print(x[-1])
print(x[-2])
tmed = t[-1]+t[-2]/2
print(tmed)
print(vx[-1])
plt.plot(t,vx, label="velocity")
plt.grid()
