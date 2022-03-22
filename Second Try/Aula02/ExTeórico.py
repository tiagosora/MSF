import numpy as np
import matplotlib.pyplot as plt

t0 = 0
x0 = 0
vx0 = 0
g = 10  
dt = 0.1
n = 20
a = +g
xt = []
xt.append(x0)
t = np.linspace(0,n*dt,n+1)
vxt = g*t

for i in range(1,n+1):
    xt.append(xt[i-1] + vxt[i]*dt)
     
xtT = []
xtT.append(x0)

for i in range(1,n+1):
    xtT.append(0.5*g*pow(t[i],2))

plt.plot(t,vxt)
plt.plot(t,xt,".")
plt.plot(t,xtT,".")
plt.show()