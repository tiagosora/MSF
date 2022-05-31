# -*- coding: utf-8 -*-
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
m = 1000

w = np.sqrt(k/m)

t = np.arange(0, 500+dt, dt)
psi = 0
A = 4

x = A*np.cos(w*t+psi)

plt.plot(t,x)

rx = np.zeros(t.size)
v = np.zeros(t.size)
rx[0] = 4
for i in range(t.size-1):
    a = -k*rx[i]
    v[i+1] = v[i] + a*dt
    rx[i+1] = rx[i]+v[i]*dt
    
    
    
    
plt.plot(t,x)
plt.plot(t,rx)