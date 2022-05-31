# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:57:14 2022

@author: draki
"""


import matplotlib.pyplot as plt
import numpy as np

vi = 10 # m/s
dt = 0.001
T = np.arange(0,2.2+dt, dt)
y = T*(10.0 - 4.9*T)

v = 10 + -9.8*T

print((-10/-9.8)*(10.0 - 4.9*(-10/-9.8)))
floor = np.zeros(T.size)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(T, y, label='Position no air resis, dt = 0.001')
ax.plot(T, floor, label="Y = 0")
ax.plot((-10/-9.8), (-10/-9.8)*(10.0 - 4.9*(-10/-9.8)), 'x', label='Highest point')
plt.legend()