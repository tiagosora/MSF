# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:25:36 2022

@author: draki
"""
import matplotlib.pyplot as plt
import numpy as np

#9 mins
y = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329]) #DistanceKM
N = y.size
Time = np.linspace(0, N-1, 10) # OR  np.array([0,1,2,3,4,5,6,7,8,9])
x = Time/60 #Time in hours

xy = x*y
xx = np.square(x)
yy = np.square(y)

Sumx = x.sum()
Sumy = y.sum()
Sumxy = xy.sum()
Sumxx = xx.sum()
Sumyy = yy.sum()

m = ((N * Sumxy) - (Sumx * Sumy))/(N * Sumxx - (Sumx)**2) # declive

b = ((Sumxx * Sumy) - (Sumx * Sumxy))/(N * Sumxx - (Sumx)**2) # coordenada na origem

r2_top_numerator = ((N*Sumxy) - (Sumx*Sumy))**2 
r2_top_denominator = ((N*Sumxx)-(Sumx)**2)*((N*Sumyy) - (Sumy)**2)

r2 = r2_top_numerator/r2_top_denominator # coeficiente

deltamSquareroot = np.sqrt(((1/r2)-1)/(N-2))
deltam = abs(m)*deltamSquareroot # erro de m

deltabSquareroot = np.sqrt(Sumxx/N)
deltab = deltam * deltabSquareroot # erro de b


Median_vel = y[N-1]/x[N-1] # Velocidade media (yf - y0)/(xf - x0); x0 e y0 = 0
print(Median_vel)
poly_test = np.poly1d(np.polyfit(x,y, 1 )) # np.polyfit para dar os valores de x^n e np.poly1d para utilizar como uma funçao 
#chamar poly_test(x) com x sendo um array do numpy ! ! ! Provavelmente Inutil ! ! !


xmax = np.max(x)*1.1
xmin = np.min(x)*0.9
ymax = np.max(y)*1.1
ymin = np.min(y)*0.9
x1 = np.array([xmin,xmax])
yline = m*x1+b

fig1, ax = plt.subplots(1, 2, figsize=(13,6), layout="constrained")

ax[0].plot(x,y,"o")
ax[0].plot(x,poly_test(x)) # exemplo de como usar poly_test(x)
ax[0].set_xlim([xmin,xmax])
ax[0].set_ylim([ymin,ymax])

ax[1].plot(x,y,"o",x1,yline)
ax[1].set_xlim([xmin,xmax])
ax[1].set_ylim([ymin,ymax])