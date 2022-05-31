# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:38:36 2022

@author: draki
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119])
x = np.array([0,5,10,15,20,25,30,35,40,45])

#plt.plot(x,y) mostra que o grafico é exponecial, daí aplicamos log no array de y, pois a funçao tem o aspeto y = y0*e^(p*x)
#aplicando log ficaria log(y) = log(y0) + p * t, onde p é uma constante e t é o nosso eixo x.

logy = np.log(y)

#depois de aplicar os logs é fazer a regressão linear como normal

N = x.size

xy = x*logy
xx = np.square(x)
yy = np.square(logy)

Sumx = x.sum()
Sumy = logy.sum()
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

xmax = np.max(x)*1.1
xmin = np.min(x)*0.9
ymax = np.max(logy)*1.1
ymin = np.min(logy)*0.9
x1 = np.array([xmin,xmax])
yline = m*x1+b

fig1, ax = plt.subplots(1, 2, figsize=(13,6), layout="constrained")

ax[0].(x, y, "o")


ax[1].plot(x,logy,"o",x1,yline)
