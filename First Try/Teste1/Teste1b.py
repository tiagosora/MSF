import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

M = [0.15 , 0.20 , 0.16 , 0.11 , 0.25 , 0.32 , 0.40 , 0.45 , 0.50 , 0.55]
T = [1.21 , 1.40 , 1.26 , 1.05 , 1.60 , 1.78 , 2.00 , 2.11 , 2.22 , 2.33]

logx=np.log(T)
logy=np.log(M)

N = len(logx)

sumxy = 0
for i in range(N):
    sumxy += logy[i] * logx[i]

sumx = sum(a for a in logx)
sumy = sum(b for b in logy)
sumxsquare = sum(a**2 for a in logx)
sumysquare = sum(b**2 for b in logy)

m = (N * sumxy - sumx * sumy) / (N * sumxsquare - (sumx)**2)

b = (sumxsquare * sumy - sumxy * sumx) / (N * sumxsquare - (sumx)**2)

r = (sumxy - ((sumx * sumy) / N)) / math.sqrt((sumxsquare - (sumx**2/ N)) * (sumysquare - (sumy**2 / N)))

xmax=np.max(logx)*1.1
xmin=np.min(logx)*0.9

x=np.linspace(xmin,xmax,1000)
y=m*x+b
plt.plot(logx,logy,'o',x,y)
plt.show()
