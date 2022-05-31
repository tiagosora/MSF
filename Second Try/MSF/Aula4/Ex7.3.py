# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:02:22 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

vi = 10 # m/s
dt = 0.001
T = T = np.arange(0,2.2+dt, dt)
y = T*(10.0 - 4.9*T)

v = 10 + -9.8*T

print(10.0/4.9)
floor = np.zeros(T.size)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(T, y, label='Position no air resis, dt = 0.001')
ax.plot(T, floor, label="Y = 0")
ax.plot((10.0/4.9), (10.0/4.9)*(10.0 - 4.9*(10.0/4.9)), 'x', label='Return to 0')
plt.legend()