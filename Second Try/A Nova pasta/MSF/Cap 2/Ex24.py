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
v0 = 55.55

g = 9.80 ##aceleração gravitica

## Passo temporal para o Método de Euler
dt = 0.001 ##passo temporal
t0 = 0.00 ##tempo inicial
tf = 5.00 ##tempo final
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

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
ax[0] = g - D*vx[0]*np.abs(vx[0])

## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    vv = np.abs(vx[i])
    ax[i+1] = g - D*vx[i]*vv

    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

graph(t,x,"Lei da Posição", "Tempo (s)", "Y (m)")
plt.show()
graph(t,ax,"Lei da Aceleração", "Tempo (s)", "Aceleração (m²/s)")

graph(t,vx,"Lei da Velocidade", "Tempo (s)", "Velocidade (m/s)")


## Alínea b) 
for i in range(N):
    if t[i+1] > 1-dt and  t[i+1] < 1+dt:
        print('A velocidade ao final de 1 segundo é {:.1f} m/s, calculando recorrendo-se ao método de Euler com um passo de {:.3f}s.'.format(vx[i+1], dt))
        break

## Alínea c)
vmetade = v0/2

for i in range(N):
    if vx[i+1] > vmetade-1 and  vx[i+1] < vmetade+1:
        print('O volante tem a sua velocidade reduzida em metade após {:.3f}s.'.format(t[i+1], dt))
        break

## Alínea d)

for i in range(N):
    if x[i+1] > 4-0.1 and  x[i+1] < 4+0.1:
        print('O volante demora {:.3f}s a percorrer 4m.'.format(t[i+1], dt))
        break