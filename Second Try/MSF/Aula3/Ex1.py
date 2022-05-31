# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:09:36 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

a = 2 # 2ms = 7.2 Km/h
vecC = 70/3.6 # velocidade do carro A
T = np.linspace(0,30,301) # criar array de 0 a 30 segundos com 300 divisões
Tsquared = np.square(T) # array do tempo^2

Xpolicia = 1/2*a*Tsquared # x = x0 + v0*t + 1/2*a*Tsquared, x0 = 0, v0 = 0

Xcarro = vecC*T # X do carro A, a aceleraçao é nula, logo velocidade constante

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(T, Xcarro, label='Carro A')
ax.plot(T, Xpolicia, label='Carro Patrulha')
plt.legend()

tenc = ( 2 * vecC ) / a # igualar iquaçoes de Xpolicia e Xcarro e resolver para t
xenc = tenc * vecC # posiçao de interseçao da posiçoes do carro

ax.plot(tenc, xenc, "ro", label='Ponto de encontro')
