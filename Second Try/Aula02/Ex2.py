from cProfile import label
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


# b)
m = (N*sumxiyi-sum(t)*sum(yt))/(N*sumxi2-pow(sum(t),2))
print("m =", str (m))

b = (sumxi2*sum(yt)-sum(t)*sumxiyi)/(N*sumxi2-pow(sum(t),2))
print("b =", str (b))   

yD = []
for i in range(N):
    yD.append(m*t[i]+b)

# c)
vt = []
at = []

for i in range(N-1):
    vt.append((yt[i+1]-yt[i])/dt)

for i in range(N-2):
    at.append((vt[i+1]-vt[i])/dt)

# d)
at2 = []

for i in range(N-1):
    at2.append(g-(g/pow(vT,2)*vt[i]*abs(vt[i])))

# plt.plot(t,yt,".",label="p")
# plt.plot(t[:-1],vt,".",label="v")
# plt.plot(t[:-2],at,".",label="a")
# plt.plot(t[:-1],at2,".",label="a2")
# plt.legend()
# plt.show()

# e)

y = 0
i = 0
ya = []
while(y<20):
    y = (pow(vT,2)/g)*math.log(math.cosh((g*i)/vT))
    ya.append(y)
    i += dt

print("time it took:", len(ya)/(1/dt), "seg with resistance")

vt = []
at = []

for i in range(len(ya)-1):
    vt.append((ya[i+1]-ya[i])/dt)

for i in range(len(ya)-2):
    at.append((vt[i+1]-vt[i])/dt)

print("v =", vt[-1])
print("a =", at[-1])

y = 0
i = 0
ya = []
a = g
while(y<20):
    y = y0 + vy0*i + 0.5*a*pow(i,2)
    ya.append(y)
    i += dt

print("time it took:", len(ya)/(1/dt), "seg without resistance")

vt = []
at = []

for i in range(len(ya)-1):
    vt.append((ya[i+1]-ya[i])/dt)

for i in range(len(ya)-2):
    at.append((vt[i+1]-vt[i])/dt)

print("v =", vt[-1])
print("a =", at[-1])
