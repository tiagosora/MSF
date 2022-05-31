# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 03:04:39 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

T = np.linspace(0,4,41)
g = 9.8
Vterminal = 6.80 # m/s
t = 3.2
vt = 6.80
t = 3.4221 # tempo aproximado de quando o volante antige o solo, usar 
y = 20 - ((Vterminal*Vterminal)/g * np.log(np.cosh((g*T)/Vterminal))) # posiçao inicial - a equaçao da posiçao (dunno why it works, se calhar está mal)

velocity = vt*np.tanh(g*t/vt) # equaçao de velocidade

ace = g/np.cosh(g*t/vt)**2 # equaçao de acelaraçao 

print(velocity, ace) # valores da velocidade e aceleraçao quando o volante chega ao solo ( velocidade deve estar proximo da velocidade terminal e
                     # a aceleração deve estar perto de 0)

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

for i in range(0, T.size): #Nao pode passar do solo
    if y[i]<0:
        y[i] = 0

ax.set_xlabel('tempo (s)')
ax.set_ylabel('Y (m)')
ax.plot(T, y, label='Posição do Volante')
plt.legend()