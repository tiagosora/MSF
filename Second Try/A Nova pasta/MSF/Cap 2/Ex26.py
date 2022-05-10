import matplotlib.pyplot as plt
import numpy as np

# Função utilizada para obter gráficos simples
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
v0 = 0

g = 9.80 ##aceleração gravitica

## Passo temporal para o Método de Euler
dt = 0.0001 ##passo temporal
t0 = 0.00 ##tempo inicial
tf = 15 ##tempo final
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

## Alínea a)

## Resistência do Ar
vt = 5
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

graph(t,x,"Método de Euler","Tempo (s)","Posição (m)")
plt.show()


for i in range(N):
    if x[i+1] > 54.1-0.01 and  x[i+1] < 54.1+0.01:
        print('O paraquedista demora {:.3f}s a atingir o solo, à velocidade de {:.3f} m/s.'.format(t[i+1], vx[i+1]))
        break

