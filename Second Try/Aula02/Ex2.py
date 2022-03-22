import numpy as np
import matplotlib.pyplot as plt
import math


vy0 = 0
y0 = 0
g = 10
dt = 0.1
N = 40
t = np.linspace(0,4,N)
vT = 6.8
yt = []

for i in range(N):
    yt.append((pow(vT,2)/g)*math.log(math.cosh((g*t[i])/vT)))

sumxiyi = 0
for i in range(N):
    sumxiyi = sumxiyi + (t[i]*yt[i])

sumxi2 = 0
for i in range(N):
    sumxi2 = sumxi2+ (pow(t[i],2))

sumyi2 = 0
for i in range(N):
    sumyi2 = sumyi2+ (pow(yt[i],2))

m = (N*sumxiyi-sum(t)*sum(yt))/(N*sumxi2-pow(sum(t),2))
print("m =", str (m))

b = (sumxi2*sum(yt)-sum(t)*sumxiyi)/(N*sumxi2-pow(sum(t),2))
print("b =", str (b))   

yD = []
for i in range(N):
    yD.append(m*t[i]+b)

plt.plot(t,yt)
plt.show()