import numpy as np
import matplotlib.pyplot as plt
import math

def graph(x,y,title = "Gráfico", xaxis = "Eixo X", yaxis = "Eixo Y"):
    plt.plot(x,y,'o')

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)

# máximo pelo polinómio de Lagrange
def maximo(xm1,xm2,xm3,ym1,ym2,ym3): 
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xmax=0.5*xmla/(a+b+c)

    xta=xmax-xm1
    xtb=xmax-xm2
    xtc=xmax-xm3

    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xmax, ymax

# raiz pelo polinómio de Lagrange
def zerosv(xm1,xm2,xm3,ym1,ym2,ym3):  
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    am=a+b+c
    bm=a*(xm2+xm3)+b*(xm1+xm3)+c*(xm1+xm2)
    cm=a*xm2*xm3+b*xm1*xm3+c*xm1*xm2

    xzero=(bm+np.sqrt(bm*bm-4*am*cm))/(2*am)
    if xm3 > xm1 and (xzero < xm1 or xzero > xm3): 
        xzero=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)


    if xm1 > xm3 and (xzero < xm3 or xzero > xm1):
        xzero=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)

    xta=xzero-xm1
    xtb=xzero-xm2
    xtc=xzero-xm3
    yzero=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xzero, yzero

x0 = 0
y0 = 0
z0 = 23.8

vx0 = 25
vy0 = 5
vz0 = -50

g = 9.80 ##aceleração gravitica

## Implementando a Força de Magnus
r = 0.11
dAr = 1.225
A = (math.pi)*(r**2)
Mx0 = 0.5*A*r*dAr*-20000
My0 = 0
Mz0 = 0.5*A*r*dAr*-10000
m = 0.45

## Passo temporal para o Método de Euler
dt = 0.001 ##passo temporal
t0 = 0.00 ##tempo inicial
tf = 20.00 ##tempo final
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.

## NOTA: Vx é constante s/ resistência do ar (igual a Vx0)
t = np.zeros(N+1)

ax = np.zeros(N+1)
ay = np.zeros(N+1)
az = np.zeros(N+1)

vx = np.zeros(N+1)
vy = np.zeros(N+1)
vz = np.zeros(N+1)

x = np.zeros(N+1)
y = np.zeros(N+1)
z = np.zeros(N+1)

Mx = np.zeros(N+1)
My = np.zeros(N+1)
Mz = np.zeros(N+1)

vz[0] = vz0
vy[0] = vy0
vx[0] = vx0

x[0] = x0
y[0] = y0
z[0] = z0

Mx[0] = Mx0
My[0] = My0
Mz[0] = Mz0

## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    Mx[i+1] = 0.5*A*r*dAr*-400*vx[i]
    My[i+1] = 0
    Mz[i+1] = 0.5*A*r*dAr*-400*vz[i]

    az[i+1] = Mz[i]/m
    ax[i+1] = Mx[i]/m
    ay[i+1] = -g + My[i]/m

    vz[i+1] = vz[i] + az[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    z[i+1] = z[i] + vz[i]*dt

graph(t,y)
plt.show()

for i in range(N):
    if x[i] < 0 and (z[i]>0 and z[i]<7.3) and (y[i]>0 and y[i]<2.4):
        print('Entrou')
        break