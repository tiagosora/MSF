# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:02:37 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

t0 = 0
x0 = 0
v0x= 0
g = 9.8
deltaT = 0.1
N = 20

t = np.linspace(0,2,21)
xAproximation = [0]*(N+1)
xExact = 1/2*g*t**2


fig = plt.figure()
ax = fig.add_subplot(1,1,1)


for i in range(1, N+1):
    vplaceholder = g*(i-1)*deltaT
    xAproximation[i] = xAproximation[i-1]+vplaceholder*deltaT
    

ax.set_xlabel('tempo (s)')
ax.set_ylabel('Y (m)')
ax.plot(t, xExact, label="posicao exato")
ax.plot(t, xAproximation,"x", label="deltat = 0.1")

plt.legend()