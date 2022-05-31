# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:44:22 2022

@author: draki
C) -->
"""
import matplotlib.pyplot as plt
import numpy as np

dt = 0.01 #10 vezes menor que 0.1
g = 9.8
T = np.arange(0,4+dt, dt)
v = np.zeros(T.size)

for i in range(0, T.size-1):
    v[i+1] = v[i] + g*dt

v_a = g*T

fig1, ax = plt.subplots(1, 2, figsize=(13,6),layout="constrained")

ax[0].set_xlabel('tempo (s)')
ax[0].set_ylabel('X (m)')
ax[0].plot(T, v, label='Velocity')

ax[1].set_xlabel('tempo (s)')
ax[1].set_ylabel('X (m)')
ax[1].plot(T, v_a, label='Velocity')


