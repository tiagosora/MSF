# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:45:34 2022

@author: draki
"""
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,4,40)
g = 9.8
vt = 6.80 # m/s

velocity = vt*np.tanh(g*t/vt) # equaçao da velocidade com velocidade terminal ( derivada da equaçao de posiçao )

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('v (m/s)')
ax.plot(t, velocity, label='Posição do Volante')
plt.legend()
