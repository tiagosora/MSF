import math
import numpy as np
import matplotlib.pyplot as plt
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

#dados iniciais
massa = 1
dist = [6.37, 7.02, 7.61, 8.02, 8.43, 8.92, 9.31, 9.78, 10.25, 10.74]
aceleracao = [9.8, 8.0, 6.6, 6.3, 5.5, 5.1 , 4.6, 4.1, 3.8, 3.6]
distancia=[1/((n * 10**6)**2) for n in dist]


#y= a
#x=1/r^2 

plt.plot(distancia, aceleracao, 'ro')
xmax=np.max(distancia)*1.1
xmin=np.min(distancia)*0.9

lin_reg = stats.linregress(distancia, aceleracao) #lista com o declive, ordenada, valor de r, ?, delta m, deltab 
x = np.linspace(xmin, xmax, 100)#Gerar array com 100 valores 
plt.plot(x, x * lin_reg.slope + lin_reg.intercept)
plt.xlabel('1/R^2')
plt.ylabel('Aceleração')
plt.title('Exercício 10 MSF')
plt.grid(False)
plt.show()


print("K: ",dadosgraficos(distancia,aceleracao)["m"], " +/- " , dadosgraficos(distancia,aceleracao)["deltam"])



