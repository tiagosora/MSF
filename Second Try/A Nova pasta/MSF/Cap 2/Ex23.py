import numpy as np
import matplotlib.pyplot as plt
import math

def graph(x,y,title = "Gráfico", xaxis = "Eixo X", yaxis = "Eixo Y"):
    plt.plot(x,y,'o')

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)

y0 = 0
v0 = 0

g = 9.80 ##aceleração gravitica

## Passo temporal para o Método de Euler
dt = 0.01 ##passo temporal
t0 = 0.00 ##tempo inicial
tf = 4.00 ##tempo final
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.

t = np.zeros(N+1)

vy = np.zeros(N+1)
y = np.zeros(N+1)

vy[0] = v0
y[0] = y0


## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    vy[i+1] = vy[i] + g*dt

    y[i+1] = y[i] + vy[i]*dt

graph(t,y,"Queda da pena","Tempo (s)","Posição (m)")
plt.show()

## Alínea b)
for i in range(N):
    if t[i+1] > 3-2*dt and  t[i+1] < 3+2*dt:
        print('A velocidade ao final de 3 segundos é {:.1f} m/s, calculando recorrendo-se ao método de Euler com um passo de {:.3f}s.'.format(vy[i+1], dt))
        break

## Alínea c)
for i in range(N):
    if t[i+1] > 2-2*dt and  t[i+1] < 2+2*dt:
        print('A posição ao final de 2 segundos é {:.1f} m, calculando recorrendo-se ao método de Euler com um passo de {:.3f}s.'.format(y[i+1], dt))
        break
