# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:45:16 2022

@author: draki
h)
"""
import matplotlib.pyplot as plt
import numpy as np


xdt1 = -18.62
xdt2 = -19.502
xanalitical = -19.6

T = np.arange(0, 0.12, 0.001)
error1 = np.abs(xdt1 - xanalitical) # y1
error2 = np.abs(xdt2 - xanalitical) # y2
errorarry = [error2, error1]
Tarray = [0.01, 0.1]
m = (error2 - error1)/(0.01-0.1) # declive dos erros y2-y1/x2-x1, x1 = 0.1, x2 = 0.01; y2 = |valorobtido - valoranalitico|

y = m*T # reta, b = 0 porque quando mais proximo o dt for de 0 menor é o erro, logo lim dt = 0 entao o desvio é 0, coordenada (0,0)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('deltaT (s)')
ax.set_ylabel('Desvio (m)')
ax.plot(T, y, label='b forçado = 0')
ax.plot(0, 0, "bo", label='exato')
ax.plot(Tarray, errorarry, "x", label='exato')
