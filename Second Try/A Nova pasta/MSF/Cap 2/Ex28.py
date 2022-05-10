import matplotlib.pyplot as plt
import numpy as np

# Função utilizada para obter gráficos simples
def graph(x,y,title = "Gráfico", xaxis = "Eixo X", yaxis = "Eixo Y"):
    plt.plot(x,y,'o')

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)

x0 = 0
v0 = 0

g = 9.80 ##aceleração gravitica

## Passo temporal para o Método de Euler
dt = 0.0001 ##passo temporal
t0 = 0.00 ##tempo inicial
tf = 15 ##tempo final
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

## PENA DE BADMINTON

## Resistência do Ar
vt = 6.80
D = g/vt**2

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.

t = np.zeros(N+1)

ax = np.zeros(N+1)
vx = np.zeros(N+1)
x = np.zeros(N+1)

vx[0] = v0
x[0] = x0

## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    vv = np.abs(vx[i])
    ax[i+1] = g - D*vx[i]*vv

    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

## Gráfico posição*tempo

plt.subplot(1,2,1)
graph(t,x,"Pena de Badminton","Tempo (s)","Posição (m)")



for i in range(N):
    if x[i+1] > 5-0.001 and  x[i+1] < 5+0.001:
        print('A pena demora {:.3f}s a atingir o solo, à velocidade de {:.3f} m/s.'.format(t[i+1], vx[i+1]))
        break

## BOLA DE TENIS
## Resistência do Ar
vt = 27.77
D = g/vt**2

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.

t = np.zeros(N+1)

ax = np.zeros(N+1)
vx = np.zeros(N+1)
x = np.zeros(N+1)

vx[0] = v0
x[0] = x0

## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    vv = np.abs(vx[i])
    ax[i+1] = g - D*vx[i]*vv

    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

## Gráfico posição*tempo
plt.subplot(1,2,2)
graph(t,x,"Bola de Ténis","Tempo (s)","Posição (m)")
plt.show()


for i in range(N):
    if x[i+1] > 5-5*dt and  x[i+1] < 5+5*dt:
        print('A bola demora {:.3f}s a atingir o solo, à velocidade de {:.3f} m/s.'.format(t[i+1], vx[i+1]))
        break