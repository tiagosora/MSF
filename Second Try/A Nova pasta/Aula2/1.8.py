# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:52:47 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 

#9 mins
T = np.array([200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]) #Temperature
E = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7]) #Energy

# se dermos graph dos pontos anteriores notaremos que é uma função exponencial, daí aplicamos os logaritmos 

x = np.log(T) 
y = np.log(E)
N = x.size

#depois de aplicar os logs é fazer a regressão linear como normal

xy = x*y
xx = np.square(x)
yy = np.square(y)

Sumx = x.sum()
Sumy = y.sum()
Sumxy = xy.sum()
Sumxx = xx.sum()
Sumyy = yy.sum()

m = ((N * Sumxy) - (Sumx * Sumy))/(N * Sumxx - (Sumx)**2)

b = ((Sumxx * Sumy) - (Sumx * Sumxy))/(N * Sumxx - (Sumx)**2)

r2_top_numerator = ((N*Sumxy) - (Sumx*Sumy))**2
r2_top_denominator = ((N*Sumxx)-(Sumx)**2)*((N*Sumyy) - (Sumy)**2)

r2 = r2_top_numerator/r2_top_denominator

deltamSquareroot = np.sqrt(((1/r2)-1)/(N-2))
deltam = abs(m)*deltamSquareroot

deltabSquareroot = np.sqrt(Sumxx/N)
deltab = deltam * deltabSquareroot


Median_vel = y[N-1]/x[N-1]  

poly_test = np.polyfit(x,y, 1   )


xmax = np.max(x)*1.1
xmin = np.min(x)*0.9
ymax = np.max(y)*1.1
ymin = np.min(y)*0.9
x1 = np.array([xmin,xmax])
yline = m*x1+b

fig1, ax = plt.subplots(1, 2, figsize=(13,6), layout="constrained")

ax[0].plot(x, y, "o")
ax[0].set_xlim([xmin,xmax])
ax[0].set_ylim([ymin,ymax])

ax[1].plot(x,y,"o",x1,yline)
ax[1].set_xlim([xmin,xmax])
ax[1].set_ylim([ymin,ymax])