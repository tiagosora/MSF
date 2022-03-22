import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

D = [4.07, 3.69, 3.16, 2.76, 2.48, 2.27, 2.12]
V = [1.32, 1.61, 2.17, 2.83, 3.49, 4.15, 4.72]

logx=[x for x in V]
logy=[x**2 for x in D]

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

print(m)
print(b)
print(r)

xmax=np.max(logx)*1.1
xmin=np.min(logx)*0.9

x=np.linspace(xmin,xmax,1000)
y=m*x+b
plt.plot(logx,logy,'o',x,y)
plt.show()