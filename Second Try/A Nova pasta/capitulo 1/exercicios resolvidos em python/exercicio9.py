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
atividade = [9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119]
t = [c * 5 for c in range(0, len(atividade))]

print("-------alinea(a)-------")
plt.plot(t,atividade,"ro")
plt.xlabel('Tempo(dias)')
plt.ylabel('Atividade (mCi)')
plt.title('Exercício 09 MSF')
plt.show()
#Relação entre a atividade e o tempo não é linear
print("------------------------")

print("-------alinea(b)-------")
loga=np.log(atividade)
#valores negativos
xmax=np.max(t)*1.1
xmin=np.min(t)*0.9

lin_reg = stats.linregress(t, loga) #lista com o declive, ordenada, valor de r, ?, delta m, deltab 
x = np.linspace(xmin, xmax, 100)#Gerar array com 100 valores 
plt.plot(x, x * lin_reg.slope + lin_reg.intercept)
plt.xlabel('Tempo(dias)')
plt.ylabel('log/Atividade (mCi)')
plt.title('Exercício 09 MSF')
plt.plot(t, loga, "ro")
plt.show()

print("declive: ",dadosgraficos(t,loga)["m"], " +/- " , dadosgraficos(t,loga)["deltam"])
