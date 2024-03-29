import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


dt=0.01                 # INPUT 
tf=4.0
t0=0
n=np.int((tf-t0)/dt+0.1)
print('n',n)

t=np.zeros(n+1)
vy=np.zeros(n+1)
y=np.zeros(n+1)

g=9.80
v0y=0
y0=0
t[0]=t0
vy[0]=v0y
y[0]=y0
# b
for i in range(n):
    t[i+1]=t[i]+dt
    vy[i+1]=vy[i]+g*dt       
    y[i+1]=y[i]+vy[i]*dt    # +1/2*g*dt**2

for i in range(n):
    if t[i+1] > 3-2*dt and  t[i+1] < 3+2*dt:
        print('dt, t, vy = ',dt,t[i+1],vy[i+1])
        
for i in range(n):
    if t[i+1] > 2-2*dt and  t[i+1] < 2+2*dt:
        print('dt, t, y = ',dt,t[i+1],y[i+1])