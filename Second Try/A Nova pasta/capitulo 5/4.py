import matplotlib.pyplot as plt
import numpy as np
import math
import sympy as sym
from scipy import stats


def dadosgraficos(x,y):
    n=len(x)
    sumx=sum(x)
    sumy=sum(y)
    xy=sum(x[i]*y[i] for i in range(n))
    xx=sum(x[i]**2 for i in range(n))
    yy=sum(y[i]**2 for i in range(n))

    m=((n*xy)-(sumx*sumy))/((n*xx)-(sumx**2))
    b=((xx*sumy)-(sumx*xy))/((n*xx)-(sumx**2))
    r2=(((n*xy)-(sumx*sumy))**2)/(((n*xx)-(sumx**2))*((n*yy)-(sumy**2)))
    deltam=abs(m)*math.sqrt(((1/r2)-1)/(n-2))
    deltab= deltam* math.sqrt(xx/n)

    return {'m':m,'b':b,'r2':r2,'deltam':deltam,'deltab':deltab}

def main (dx):
    xf=2
    xi=0
    n=int((xf-xi)/dx)
    x=np.linspace(xi,n*dx,n+1)
    valorT=1

    fx=x**3/4

    integral=dx*((fx[0]+fx[n])*0.5+np.sum(fx[1:n]))

    erro=abs(valorT-integral)

    #print(integral,erro)

    return erro

valores=[]
valores.append(main(0.2))
valores.append(main(0.1))
valores.append(main(0.02))
valores.append(main(0.002))

print(valores)

logx= np.log([0.2,0.1,0.02,0.002])
logy= np.log(valores)

#valores negativos
xmax=np.max(logx)+np.abs((np.min(logx)*0.1))
xmin=np.min(logx)-np.abs((np.min(logx)*0.1))
lin_reg = stats.linregress(logx, logy) #lista com o declive, ordenada, valor de r, ?, delta m, deltab 
x = np.linspace(xmin, xmax, 100)#Gerar array com 100 valores 
plt.plot(x, x * lin_reg.slope + lin_reg.intercept)
plt.plot(logx, logy, "ro")
plt.show()

print (dadosgraficos(logx,logy))
