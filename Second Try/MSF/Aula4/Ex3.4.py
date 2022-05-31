# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:16:38 2022

@author: draki

F) -->
"""


import matplotlib.pyplot as plt
import numpy as np

dt = 0.1
g = -9.8
T = np.arange(0,3+dt, dt)
x = np.zeros(T.size)
v = np.zeros(T.size)


for i in range(0, T.size-1):
    v[i+1] = v[i] + g * dt
    x[i+1] = x[i] + v[i] * dt



fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(T, x, label='Position, dt = 0.1')
print(x[T == 2], "m with dt =", dt)
dt = 0.01
g = -9.8
T = np.arange(0,3+dt, dt)
x = np.zeros(T.size)
v = np.zeros(T.size)


for i in range(0, T.size-1):
    v[i+1] = v[i] + g * dt
    x[i+1] = x[i] + v[i] * dt

x_a = -4.9*T**2

ax.plot(T, x, label='Position, dt = 0.01')

ax.plot(T, x_a, label='Analitical Position')

plt.legend()
print(x[T == 2], "m with dt =", dt)
print(x_a[T == 2], "m in analitical")

"""
G) Quanto menor o dt for, maior a aproximação do método de euler do valor analítico.
    

    

"""