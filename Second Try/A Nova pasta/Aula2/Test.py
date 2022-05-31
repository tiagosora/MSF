# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:03:46 2022

@author: draki
"""
import matplotlib.pyplot as plt

import numpy as np

step = 0.1
maxvalue = 3

x = np.array([])
y = np.array([])

g = 9.8
tempx = 0

function = ((6.8**2)/g) * (np.log(np.cosh((g*tempx)/6.8))) # funçao da posiçao pela integraçao analitica da velocidade
# a = g - g / (vTerminal^2) * Vy * | Vy | , Vy é velocidade no ponto y ( esta formula é util para o metodo de euler ) 
# y = ((vTerminal)/g) * (log(cosh((g*t)/vTerminal)))

while tempx <= maxvalue:
    x = np.append(x, tempx)
    y = np.append(y, function)
    function = ((6.8**2)/g) * (np.log(np.cosh((g*tempx)/6.8)))
    tempx += step

# calcula os valores do tempo e da velocidade de acordo com a funcao

plt.plot(x,y)
