# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:20:43 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np
dt = 0.01
SolX = 0
SolY = 0

t = np.arange(0,3+dt, dt)

Rx = np.zeros(t.size)
Ry = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)

Rx[0] = -1
Ry[0] = 0

Vx[0] = 0
Vy[0] = -2 * np.pi/1 * 1
G = 

for i in range(0, t.size-1):
    rr = np.sqrt(Rx[i]**2 + Ry[i]**2)
    Ax =            