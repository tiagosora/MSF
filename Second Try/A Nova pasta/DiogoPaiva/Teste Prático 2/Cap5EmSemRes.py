import math

import matplotlib.pyplot as plt

import numpy as np

import sympy as sym


#a)

tempo = 1
dt = 0.001
N = int(tempo/dt)
g = 9.8
t = np.linspace(0,1,1000)

m = 0.057                   #Massa do objeto
ax = 0                      #A acelaração em x é 0
ay = -g                     #A acelaração em y é -g pois estamos a considerar o solo y = 0
vx = np.empty(N)            #Criar vetores
vy = np.empty(N)
x = np.empty(N)
y = np.empty(N)
Em = np.empty(N)
v = np.empty(N)

vk = (100 * 1000)/3600      #Velocidade inicial em km/h

vx[0] = vk * np.cos(np.deg2rad(10))     #Velocidade do eixo dos x (se o angulo for de 10º com a horizontal)
vy[0] = vk * np.sin(np.deg2rad(10))     #Velocidade do eixo dos y (se o angulo for de 10º com a horizontal)
x[0] = 0
y[0] = 0

for i in range(N-1):
    v[i] = np.sqrt(vx[i]**2+vy[i]**2)   # Fórmula para a velocidade
    vx[i+1] = vx[i] + ax * dt           # Velocidade em x
    vy[i+1] = vy[i] + ay * dt           # Velocidade em y
    x[i+1] = x[i] + vx[i] * dt          #Posição x
    y[i+1] = y[i] + vy[i] * dt          #Posição y
    Em[i] = m*g*y[i] + 0.5 * m * v[i]**2    #Fórmula da energia mecânica



plt.xlabel("Tempo")
plt.ylabel("Em")
plt.plot(t,Em)
plt.show()
