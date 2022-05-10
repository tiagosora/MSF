import numpy as np
import matplotlib.pyplot as plt
import math

def graph(x,y,title = "Gráfico", xaxis = "Eixo X", yaxis = "Eixo Y"):
    plt.plot(x,y)

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)

x0 = 1
y0 = 0

vx0 = 0
vy0 = 2*math.pi

G = 4*(math.pi)**2

## Passo temporal para o Método de Euler
t0 = 0.00 ##tempo inicial
tf = 5 ##tempo final
dt = 0.001 ##passo temporal
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.

## NOTA: Vx é constante s/ resistência do ar (igual a Vx0)
t = np.zeros(N+1)
ax = np.zeros(N+1)
ay = np.zeros(N+1)
vx = np.zeros(N+1)
vy = np.zeros(N+1)
x = np.zeros(N+1)
y = np.zeros(N+1)

vy[0] = vy0
vx[0] = vx0

x[0] = x0
y[0] = y0

## Ciclo que implementa o Método de Euler-Cromer, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    r = math.sqrt(x[i]**2 + y[i]**2)

    ax[i]=-G*x[i]/r**3
    ay[i]=-G*y[i]/r**3

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    x[i+1] = x[i] + vx[i+1]*dt
    y[i+1] = y[i] + vy[i+1]*dt

graph(x,y,"Trajetória", "x (m)", "y (m)")
plt.show()