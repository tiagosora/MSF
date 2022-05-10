#a)

import numpy as np
import matplotlib.pyplot as plt

dt=0.001
tf=1.00
n=int(tf/dt+0.1)

t=np.linspace(0,tf,n+1)


g=9.80      # m/s**2
vt=100*1000/3600  # m/s
vel0=100*1000/3600  # m/s
theta=10*np.pi/180  # rad
v0x=vel0*np.cos(theta)
v0y=vel0*np.sin(theta)
x0=0
y0=0


#Aqui uso n+1 por ser mais facil interpretar a formula da integração
vel=np.empty(n+1) 
y=np.empty(n+1)
vx=np.empty(n+1)
x=np.empty(n+1)
ax=np.empty(n+1)
ay=np.empty(n+1)
vx=np.empty(n+1)
vy=np.empty(n+1)
energia=np.empty(n+1)
fun=np.empty(n+1)
aresx=np.empty(n+1)
aresy=np.empty(n+1)
int_trab_res=np.empty(n+1)

vx[0]=v0x
vy[0]=v0y
x[0]=x0
y[0]=y0
massa=0.057

D=g/vt**2



for i in range(0,n):

     vel=np.sqrt(vx[i]**2+vy[i]**2)

     aresx[i]=-D*vel*vx[i]
     ax[i]=aresx[i]
     aresy[i]=-D*vel*vy[i]
     ay[i]=aresy[i]-g
     vx[i+1]=vx[i]+ax[i]*dt
     vy[i+1]=vy[i]+ay[i]*dt

     x[i+1]=x[i]+vx[i]*dt
     y[i+1]=y[i]+vy[i]*dt
     energia[i]=0.5*massa*vel**2+massa*g*y[i]
     #pede o trabalho da força resistiva, logo so interessa essa parte da aceleração
     # W=integral(F dx)+integral(F dy)
     # dx é dado por vx*dt e dy=vy*dt
     #Assim: INTEGRACAO   W=Integral(  Fx vx + Fy * vy) dt
     #Força segundo X: segunda lei de Newton Fx=m*ax e Fy=m*ay (apenas as resistivas)

     fun[i]=massa*aresx[i]*vx[i]+massa*aresy[i]*vy[i]
     int_trab_res[i]=dt*((fun[0]+fun[n])*0.5+np.sum(fun[1:n-1])) #INTEGRACAO

     if (t[i]<0.4 and t[i+1]>0.4):
         stringPrint=str(t[i])+" "+str(int_trab_res[i])
         print (stringPrint)
     if (t[i]<0.8 and t[i+1]>0.8):
         stringPrint=str(t[i])+" "+str(int_trab_res[i])
         print (stringPrint)

#Calcular o ultimo valor da energia mecanica:
vel=np.sqrt(vx[i+1]**2+vy[i+1]**2)
energia[i+1]=0.5*massa*vel**2+massa*g*y[i+1]

#Calcular o ultimo valor do trabalho:
fun[i+1]=massa*aresx[i+1]*vx[i+1]+massa*aresy[i+1]*vy[i+1]
int_trab_res[i+1]=dt*((fun[0]+fun[n])*0.5+np.sum(fun[1:n-1]))

print(energia[0],energia[int(0.4/dt)],energia[int(0.8/dt)])

plt.figure()
plt.plot(t,int_trab_res,label='W Res')
plt.ylabel('W_Res (J)')
plt.xlabel( 't (s)' )
plt.grid()

plt.show()