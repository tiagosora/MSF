# import numpy as np
# import matplotlib.pyplot as plt
# 
# dt = 0.001
# tf = 1.00
# n=int(tf/dt+0.1)
# t=np.linspace(0,tf,n+1)
# 
# g = 9.8
# x0 = 0
# y0 = 0
# vx0 = (100/3.6)*np.cos(np.radians(10)) 
# vy0 = (100/3.6)*np.sin(np.radians(10))
# vt = 100/3.6
# vel0= 100/3.6
# w = [0, 0, 0]
# r = 67/2/1000
# m = 0.057
# 
# x = np.zeros(n+1)
# y = np.zeros(n+1)
# vel=np.empty(n+1)
# vx = np.zeros(n+1)
# vy = np.zeros(n+1)
# ax = np.zeros(n+1)
# ay = np.zeros(n+1)
# aresx = np.zeros(n+1)
# aresy = np.zeros(n+1)
# f = np.zeros(n+1)
# int_trab_res=np.empty(n+1)
# 
# x[0] = x0
# y[0] = y0
# vx[0] = vx0
# vy[0] = vy0
# D=g/vt**2
# 
# for i in range(0,n):
#     vel=np.sqrt(vx[i]**2+vy[i]**2)
#     aresx[i]=-D*vel*vx[i]
#     ax[i]=aresx[i]
#     aresy[i]=-D*vel*vy[i]
#     ay[i]=aresy[i]-g
#     vx[i+1]=vx[i]+ax[i]*dt
#     vy[i+1]=vy[i]+ay[i]*dt
#     x[i+1]=x[i]+vx[i]*dt
#     y[i+1]=y[i]+vy[i]*dt
#     f[i]=m*aresx[i]*vx[i]+m*aresy[i]*vy[i]
#     int_trab_res[i]=dt*((f[0]+f[n])*0.5+np.sum(f[1:n-1])) #INTEGRACAO
#     if (t[i]<0.4 and t[i+1]>0.4):
#         stringPrint=str(t[i])+" "+str(w[i])
#         print (stringPrint)
#     if (t[i]<0.8 and t[i+1]>0.8):
#         stringPrint=str(t[i])+" "+str(w[i])
#         print (stringPrint)
# 
# vv=np.sqrt(vx[i+1]**2+vy[i+1]**2)
# 
# f[i+1]=m*aresx[i+1]*vx[i+1]+m*aresy[i+1]*vy[i+1]
# int_trab_res[i+1]=dt*((f[0]+f[n])*0.5+np.sum(f[1:n-1]))
# 
# print(int_trab_res[0])
# print(int_trab_res[int(0.4/dt)])
# print(int_trab_res[int(0.8/dt)])
# 

#a)

import numpy as np
import matplotlib.pyplot as plt

dt=0.0001
tf=1.00
n=int(tf/dt+0.1)
t=np.linspace(0,tf,n+1)

g=9.80
vt=100*1000/3600
vel0=100*1000/3600
theta=10*np.pi/180
v0x=vel0*np.cos(theta)
v0y=vel0*np.sin(theta)
x0=0
y0=0

vel=np.empty(n+1) 
y=np.empty(n+1)
vx=np.empty(n+1)
x=np.empty(n+1)
ax=np.empty(n+1)
ay=np.empty(n+1)
vx=np.empty(n+1)
vy=np.empty(n+1)
energia=np.empty(n+1)

vx[0]=v0x
vy[0]=v0y
x[0]=x0
y[0]=y0
massa=0.057

D=g/vt**2

for i in range(0,n): # Metodo de Euler
     vel=np.sqrt(vx[i]**2+vy[i]**2)
     ax[i]=-D*vel*vx[i]
     ay[i]=-D*vel*vy[i]-g
     vx[i+1]=vx[i]+ax[i]*dt
     vy[i+1]=vy[i]+ay[i]*dt
     x[i+1]=x[i]+vx[i]*dt
     y[i+1]=y[i]+vy[i]*dt
     energia[i]=0.5*massa*(vel**2)+massa*g*y[i]

vel=np.sqrt((vx[i+1]**2)+(vy[i+1]**2))
energia[i+1]=0.5*massa*(vel**2)+massa*g*y[i+1]


plt.figure()
plt.plot(x,y,label='Energia')
plt.grid()
# plt.show()

# b) e c)
dt = 0.001
tf = 1.00
n=int(tf/dt+0.1)
t=np.linspace(0,tf,n+1)

g = 9.8
x0 = 0
y0 = 0
vx0 = (100/3.6)*np.cos(np.radians(10)) 
vy0 = (100/3.6)*np.sin(np.radians(10))
vt = 100/3.6
vel0= 100/3.6
m = 0.057

x = np.zeros(n+1)
y = np.zeros(n+1)
vel=np.empty(n+1)
vx = np.zeros(n+1)
vy = np.zeros(n+1)
ax = np.zeros(n+1)
ay = np.zeros(n+1)
aresx = np.zeros(n+1)
aresy = np.zeros(n+1)
EnergiaMec = np.zeros(n+1)
f = np.zeros(n+1)
int_trab_res=np.empty(n+1)

x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

D=g/vt**2

for i in range(0,n): #Método de Euler
    vel=np.sqrt(vx[i]**2+vy[i]**2)
    aresx[i]=-D*vel*vx[i]
    ax[i]=aresx[i]
    aresy[i]=-D*vel*vy[i]
    ay[i]=aresy[i]-g
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    EnergiaMec[i]=0.5*m*vel**2+m*g*y[i]
    f[i]=m*aresx[i]*vx[i]+m*aresy[i]*vy[i]
    
    int_trab_res[i]=dt*((f[0]+f[n])*0.5+np.sum(f[1:n-1]))

EnergiaMec[i+1]=0.5*m*vt**2+m*g*y[i+1]

f[i+1]=m*aresx[i+1]*vx[i+1]+m*aresy[i+1]*vy[i+1]
int_trab_res[i+1]=dt*((f[0]+f[n])*0.5+np.sum(f[1:n-1]))

plt.figure()
plt.plot(t,int_trab_res,label='W Res')
plt.ylabel('W_Res (J)')
plt.xlabel( 't (s)' )
plt.grid()

print("energia mecânica nos três instantes 𝑡0 = 0, 𝑡1 = 0.4 s e 𝑡2 = 0.8 s")
print(EnergiaMec[0])
print(EnergiaMec[int(0.4/dt)])
print(EnergiaMec[int(0.8/dt)])

print(" trabalho realizado pela força de resistência do ar nos três instantes 𝑡0 = 0, 𝑡1 = 0.4 s e 𝑡2 = 0.8 s")
print(int_trab_res[0])
print(int_trab_res[int(0.4/dt)])
print(int_trab_res[int(0.8/dt)])