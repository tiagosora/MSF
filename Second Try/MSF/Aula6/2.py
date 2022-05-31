# -*- cd1ing: utf-8 -*-
"""
Created on Tue Apr 19 14:58:28 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
massa = 0.45
r = 0.11
area = np.pi*r**2
PAr = 1.225 #kg/m^3
vt = 27.7778 #m/s
t = np.arange(0,0.5+dt, dt)
g = -9.8
x = np.zeros(t.size)
vx = np.zeros(t.size)
Wx = 0
ax = np.zeros(t.size)
ay = np.zeros(t.size)
az = np.zeros(t.size)
y = np.zeros(t.size)
vy = np.zeros(t.size)
omega = 400 
z = np.zeros(t.size)
vz = np.zeros(t.size)
Wz = 0


z[0] = 23.8
vx[0] = 25.5
vy[0] = 5
vz[0] = -50



for i in range(0,t.size-1):
    t[i+1]=t[i]+dt
    vv=np.sqrt(vx[i]**2+vy[i]**2+vz[i]**2)
    dres=g/vt**2
    mag=0.5*1.225*0.11*np.pi*0.11**2
    amx=mag*omega*vz[i]/massa
    amz=-mag*omega*vx[i]/massa
    ax[i]=-dres*vv*vx[i]+amx
    ay[i]=-g-dres*vv*vy[i]
    az[i]=-dres*vv*vz[i]+amz
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    vz[i+1]=vz[i]+az[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    z[i+1]=z[i]+vz[i]*dt
    
plt.plot(t,x,label="x")
plt.plot(t,y,label="y")
plt.plot(t,z,label="z")
plt.legend()

        