import numpy as np
import matplotlib.pyplot as plt

dt = 0.1

x0A = 0
v0A = 70*1000/3600 #m/s
aA = 0
xtA = []

x0B = 0
v0B = 0
aB = 2
xtB = []
xtB = []

N = 21
t = np.linspace(0,N*dt,N)
print(t)

for i in range(N):
    xtA.append(x0A+v0A*i+0.5*aA*pow(i,2))
    xtB.append(x0B+v0B*i+0.5*aB*pow(i,2))

plt.plot(t,xtA)
plt.plot(t,xtB)
plt.show()