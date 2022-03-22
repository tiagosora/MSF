import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

M = [0.15 , 0.20 , 0.16 , 0.11 , 0.25 , 0.32 , 0.40 , 0.45 , 0.50 , 0.55]
T = [1.21 , 1.40 , 1.26 , 1.05 , 1.60 , 1.78 , 2.00 , 2.11 , 2.22 , 2.33]

N = len(T)

sumxy = 0
for i in range(N):
    sumxy += M[i] * T[i]

sumx = sum(a for a in T)
sumy = sum(b for b in M)
sumxsquare = sum(a**2 for a in T)
sumysquare = sum(b**2 for b in M)

m = (N * sumxy - sumx * sumy) / (N * sumxsquare - (sumx)**2)

b = (sumxsquare * sumy - sumxy * sumx) / (N * sumxsquare - (sumx)**2)

r = (sumxy - ((sumx * sumy) / N)) / math.sqrt((sumxsquare - (sumx**2/ N)) * (sumysquare - (sumy**2 / N)))

xmax=np.max(T)*1.1
xmin=np.min(T)*0.9

x=np.linspace(xmin,xmax,1000)
y=m*x+b
plt.plot(T,M,'o',x,y)
plt.show()
