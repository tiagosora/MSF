import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from pynverse import inversefunc

t=np.linspace(0,4.0,100) #lista de intervalos de tempo
vt=6.80 #velocidade terminal
g=9.8 #gravidade
h=20 #altura incial

print("---------alinea (a)------")
y= ((vt**2)/g)*(np.log(np.cosh((g*t)/(vt)))) #lei do movimento

plt.plot(t, y) # coloca os pontos nos graficos
plt.xlabel('t(s)') # legenda no eixo dos x
plt.ylabel('y(m)') # legenda no eixo dos y
plt.title('Queda Volante com vy(0)=0') #titulo do grafico
plt.show() #mostrar grafico 
print() 

print("---------alinea (b)------")
t1= symbols('t',real=True, positive=True)
g1= symbols('g',real=True, positive=True)
vt1= symbols('vt',real=True, positive=True)
D = diff((vt1**2/g1)*log(cosh(g1*t1/vt1)),t1)
f=simplify(D)
print(f)

vel=vt*np.tanh((g*t)/vt) #velocidade instantânea (derivada da posição) (dada em F)
plt.plot(t, vel) # coloca os pontos nos graficos
plt.xlabel('t(s)') # legenda no eixo dos x
plt.ylabel('vy(m/s)') # legenda no eixo dos y
plt.title('Queda Volante com vy(0)=0') #titulo do grafico
plt.show() #mostrar grafico 
print() 

print("---------alinea (c)------")
dvel= diff(vt1*tanh(g1*t1/vt1),t1)
#dvel= simplify(dvel)
print(dvel)

a=g/(np.cosh(g*t/vt)**2)
plt.plot(t, a)
plt.xlabel('t(s)') # legenda no eixo dos x
plt.ylabel('ay(m/s**2)') # legenda no eixo dos y
plt.title('Queda Volante com vy(0)=0') #titulo do grafico
plt.show() #mostrar grafico 
print() 

print("---------alinea (d)------")
print(dvel.equals(g1 - g1 / vt1 ** 2 * f ** 2))
print()

print("---------alinea (e)------")
altura=20
c=np.polyfit (t,y,1)
cra = (20-c[1])/c[0]
print("tempo com resistencia do ar: ",cra, "s.")
quedalivre=np.sqrt((2*-altura)/(-g))
print("tempo em queda livre: ",quedalivre, "s.") #aceleraçao =-g
print()

print("---------alinea (f)------")
veloc= vt*np.tanh((g*cra)/vt)
print(' velocidade(solo) = ',veloc)
acele=g/np.cosh(g*cra/vt)**2
print(' acelera(solo) = ',acele)