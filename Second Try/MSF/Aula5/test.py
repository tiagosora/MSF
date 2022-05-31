# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:18:33 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
dt = 0.0001
t = np.arange(0,1+dt, dt)
x= np.array([7,8.5,9.9])
y= np.array([0.1,-0.05,-0.35])
ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(x, y, "o")

poly_test = np.poly1d(np.polyfit(x,y, 2)) # np.polyfit para dar os valores de x^n e np.poly1d para utilizar como uma funçao 

ax.plot(x, poly_test(x))
