import numpy as np
import matplotlib.pyplot as plt
import math

def graph(x,y,title = "Gráfico", xaxis = "Eixo X", yaxis = "Eixo Y"):
    plt.plot(x,y,'o',label="A")

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)

x0A = 0
v0A = 19.44
a = 0.00

x0B = 0
v0B = 0
a0B = 2

## Passo temporal para o Método de Euler
dt = 0.001 ##passo temporal
t0 = 0.00 ##tempo inicial
tf = 30.00 ##tempo final
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.

t = np.zeros(N+1)

vxA = np.zeros(N+1)
xA = np.zeros(N+1)

vxB = np.zeros(N+1)
xB = np.zeros(N+1)

vxA[0] = v0A
xA[0] = x0A
vxB[0] = v0B
xB[0] = x0B

## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    vxA[i+1] = vxA[i] - a*dt
    xA[i+1] = xA[i] + vxA[i]*dt

    vxB[i+1] = vxB[i] + a0B*dt
    xB[i+1] = xB[i] + vxB[i]*dt

graph(t,xA,"Lei do Movimento","Tempo (s)", "Posição (m)")
plt.plot(t,xB,label="P")
plt.legend()
plt.show()

## Alínea b)
for i in range(N):
    if xA[i] >= xB[i] and xA[i+1] < xB[i+1]:
        print('O carro patrulha alcança o carro A na posição {:.1f}, após {:.1f}s'.format(xA[i], t[i]))
        break

