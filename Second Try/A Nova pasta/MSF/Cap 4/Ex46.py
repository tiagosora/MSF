import numpy as np
import matplotlib.pyplot as plt
import math

def graph(x,y,title = "Gráfico", xaxis = "Eixo X", yaxis = "Eixo Y"):
    plt.plot(x,y,'o')

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)


x0 = 4

v0 = 0

k = 1
g = 9.80 
m = 1

## Passo temporal para o Método de Euler
dt = 0.001 ##passo temporal
t0 = 0.00 ##tempo inicial
tf = 5.00 ##tempo final
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.

## NOTA: Vx é constante s/ resistência do ar (igual a Vx0)
t = np.zeros(N+1)

vx = np.zeros(N+1)

x = np.zeros(N+1)

ax = np.zeros(N+1)

## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    ax[i] = -k*x[i]/m

    vx[i+1] = vx[i] + ax[i]*dt

    x[i+1] = x[i] + vx[i+1]*dt


graph(t,vx,"Velocidade Euler-Cromer", "Tempo (s)", "Velocidade (m/s)")
plt.show()

