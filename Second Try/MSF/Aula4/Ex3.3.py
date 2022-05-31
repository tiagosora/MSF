# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:02:08 2022

@author: draki

x(t) = x0 + v(t)*t + 1/2 * t^2 * a
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.1
g = -9.8
T = np.arange(0,3+dt, dt)
x = np.zeros(T.size)
v = np.zeros(T.size)


for i in range(0, T.size-1): #metodo de euelr
    v[i+1] = v[i] + g * dt # v(psi + psi) = v(psi) + ac*dt, neste caso ac = g
    x[i+1] = x[i] + v[i] * dt # x(psi +psi) = x(psi) +v(psy)*dt

x_a = -4.9*T**2 # x analitico

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(T, x, label='Position, dt = 0.1')
ax.plot(T, x_a, label='Analitical Position')
plt.legend()

print(x[T == 2])