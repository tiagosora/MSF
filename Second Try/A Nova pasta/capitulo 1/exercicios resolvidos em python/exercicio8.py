import math
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats

T= [200, 300 , 400, 500, 600, 700, 800, 900, 1000, 1100]
E = [0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557, 690.7]

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

print("---------alinea (a)------")
plt.plot(T, E,"o") # coloca os pontos nos graficos
plt.xlabel('T(K)') # legenda no eixo dos x
plt.ylabel('E(J)') # legenda no eixo dos y
plt.title('Representação dos pontos experimentais') #titulo do grafico
plt.show() #mostrar grafico 
print()
#RESOSTA: A relação entre a energia emitida e a temperatura não é linear 


print("---------alinea (b)------")
logt= np.log(T)
loge=np.log(E)
xmax=np.max(logt)*1.1
xmin=np.min(logt)*0.9

lin_reg = stats.linregress(logt, loge) #lista com o declive, ordenada, valor de r, ?, delta m, deltab 
x = np.linspace(xmin, xmax, 100)#Gerar array com 100 valores 
plt.plot(x, x * lin_reg.slope + lin_reg.intercept)
plt.plot(logt, loge, "ro")
plt.show()

#Calcular o declive e a ordenada na origem com os valores de log
print(dadosgraficos(logt,loge))