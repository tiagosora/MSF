import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

D = [4.07, 3.69, 3.16, 2.76, 2.48, 2.27, 2.12]
V = [1.32, 1.61, 2.17, 2.83, 3.49, 4.15, 4.72]

N = len(V)

sumxy = 0
for i in range(N):
    sumxy += D[i] * V[i]

sumx = sum(a for a in V)
sumy = sum(b for b in D)
sumxsquare = sum(a**2 for a in V)
sumysquare = sum(b**2 for b in D)

m = (N * sumxy - sumx * sumy) / (N * sumxsquare - (sumx)**2)

b = (sumxsquare * sumy - sumxy * sumx) / (N * sumxsquare - (sumx)**2)

r = (sumxy - ((sumx * sumy) / N)) / math.sqrt((sumxsquare - (sumx**2/ N)) * (sumysquare - (sumy**2 / N)))

xmax=np.max(V)*1.1
xmin=np.min(V)*0.9

x=np.linspace(xmin,xmax,1000)
y=m*x+b
print(m)
print(b)
plt.plot(V,D,'o',x,y)
plt.show()