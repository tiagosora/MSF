# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:20:28 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

T = np.linspace(0,4,40)
g = -9.8
Vterminal = 6.80 # m/s

y = (Vterminal*Vterminal)/g * np.log(np.cosh((g*T)/Vterminal)) # equaçao de posiçao com velocidade terminal (slide aula teorica 2 no final)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('Y (m)')
ax.plot(T, y, label='Posição do Volante')
plt.legend()

#velocoidade em funçao do tempo
