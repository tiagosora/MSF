import matplotlib.pyplot as plt
import numpy as np
import math 

# Função utilizada para obter gráficos simples
def graph(x,y,title = "Gráfico", xaxis = "Eixo X", yaxis = "Eixo Y"):
    plt.plot(x,y,'o')

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)

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

## Resistência do Ar
vt = 6.80

## Alínea a)

t = np.linspace(0,20,150)
y = ((vt**2)/g)*np.log(np.cosh(g*t/vt))

plt.plot(t,y)

plt.xlabel("Tempo (s)")
plt.ylabel("Altura (m)")

plt.grid()

plt.title("Queda da pena")
plt.show()

## Alínea b)

vy = vt*np.tanh((g*t)/vt)

plt.plot(t,vy)

plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")

plt.grid()

plt.title("Gráfico da Velocidade")
plt.show()

## Alínea c)

ay = g/(np.cosh(g*t/vt))**2

plt.plot(t,ay)

plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração (m/s²)")

plt.grid()

plt.title("Gráfico da Aceleração")
plt.show()

## Alínea e)
h = 20
ext = np.exp(g*h/vt**2)

tSolo = (np.arccosh(ext)*vt)/g
print("A pena atingiu o solo no instante {:.2f}s.".format(tSolo))

tSolo2 = math.sqrt(40/9.8)
print("Sem resistência do ar, a pena atingiria o solo no instante {:.2f}s.".format(tSolo2))

## Alínea f)
vy = vt*np.tanh((g*tSolo)/vt)
print("A pena atingiu o solo com velocidade {:.2f}s.".format(vy))

ay = g/(np.cosh(g*tSolo/vt))**2
print("A pena atingiu o solo com aceleração {:.2f}s.".format(ay))