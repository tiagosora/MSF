# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:25:33 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt=0.1
tf=4.0
t0=0 
x0=0
n=np.int((tf-t0)/dt+0.1)
print('n',n)
t=np.linspace(0,4,n+1)
x=np.zeros(n+1)
g=9.80
v0x=0
vx=g*t
vx[0]=v0x
t[0]=t0 
x[0]=x0
xExact = 1/2*g*t*t

print(t)

for i in range(n): # Método de Euler
    x[i+1]=x[i]+vx[i]*dt
    
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('tempo (s)')
ax.set_ylabel('Y (m)')
ax.plot(t, x, "o", label="deltat = 0.1")
ax.plot(t, xExact, label="posiçao exato")
