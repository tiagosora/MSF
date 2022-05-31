# -*- coding: utf-8 -*-1
"""
Created on Mon May  9 17:30:26 2022

@author: draki
v =-A*w*sin(wt+d)
A =-A*w**2*cos(wt+d)
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.01

k = 1
m = 1

w = np.sqrt(k/m)

t = np.arange(0, 40+dt, dt)
psi = 0
A = 4

x = A*np.cos(w*t+psi)

plt.plot(t,x)

rx = np.zeros(t.size)
v = np.zeros(t.size)
rx2 = np.zeros(t.size)
v2 = np.zeros(t.size)
rx[0] = 4
rx2[0] = 4
for i in range(t.size-1):
    a = -k/m*rx[i]
    v[i+1] = v[i] + a*dt
    rx[i+1] = rx[i]+v[i]*dt
    

EM1 = m*(0.5*v**2 + 0.5*k*rx**2)

    

fig1, ax = plt.subplots(2, 2, figsize=(13,6), layout="constrained")

ax[0, 0].plot(t,x, t, rx)
ax[0, 1].plot(t, EM1)

for i in range(t.size-1):
    a = -k/m*rx2[i]
    v2[i+1] = v2[i] + a*dt
    rx2[i+1] = rx2[i]+v2[i+1]*dt
    

EM2 = m*(0.5*v**2 + 0.5*k*rx2**2)
ax[1, 0].plot(t,x, t, rx2)
ax[1, 1].plot(t, EM2)