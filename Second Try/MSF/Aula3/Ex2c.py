# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:48:57 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,4,4000)
g = 9.8
vt = 6.80 # m/s
ace2 = np.zeros(t.size)

v = vt*np.tanh(g*t/vt) # calculo do array da velocidade

ace = g/np.cosh(g*t/vt)**2 # equaçao da acelaração incluindo velocidade terminal (derivada da equação de velocidade)

for i in range(0, t.size-1):
    ace2[i+1] = g-g/(vt*vt)*v[i]*abs(v[i]) # usando metodo de euler para verificar se a equaçao resultante da derivada é equivalente
                                           # á equação a(t) = g - (g/vt^2) * vy * |vy|, vt = velocidade terminal, vy = velocidade do instante anterior
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('a (m/s/s)')
ax.plot(t, ace, label='Posição do Volante')
ax.plot(t, ace2, label='Posição do Volante')

plt.legend()
