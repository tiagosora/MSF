# -*- coding: utf-8 -*-
"""
Created on Mon May 23 16:55:05 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

t = np.arange(0,200+dt,dt)

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
    FRes = Cres/2*area*Par*vx[i]**2+Cyu*m*g
    F = Fcic - FRes
    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    
plt.plot(t,vx, label="velocity")

plt.grid()

print(vx[-1])
print(vx[-1]*0.9)


vx = vx - vx[-1]*0.9

plt.plot(t,vx, label="velocity -90%")

for i in range(vx.size-1):
    if(vx[i] == 0):
        print(t[np.where(vx == vx[i])])
        break;
    elif(vx[i] > 0):
        t1 = t[np.where(vx == vx[i])]
        t2 = t[np.where(vx == vx[i-1])]
        tmed = (t1+t2)/2
        print(tmed)
        break;


plt.legend()
