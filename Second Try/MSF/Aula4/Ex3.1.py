# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:13:55 2022

@author: draki
Euler method startup:
    
t = np.linspace(T0, TF, N), T0= initial time; TF= final time; N= Number of total points (dont forget t0)
t = np.arange(T0, TF+dT, dT), T0= initial time; TF+dT= final time plus size of step due to last being exclusive; dT= Size of steps 

A) acelaraçao constante, velocidade uniformemente crescente, movimento uniformemente crescente ( provavelmente dunno), relação linear
B) -->
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.1
g = 9.8
T = np.arange(0,4+dt, dt)
v = np.zeros(T.size)

for i in range(0, T.size-1): # metodo de euler
    v[i+1] = v[i] + g*dt # v(psi + psi) = v(psi) + ac*dt, nestecaso ac = g
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(T, v, label='Velocity')
plt.legend()


print(v[np.where(T == 3)])