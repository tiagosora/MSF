import math
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats

m= [0.15,0.20,0.16,0.11,0.25,0.32,0.40,0.45,0.50,0.55]
T = [1.21,1.40,1.26,1.05,1.60,1.78,2.00,2.11,2.22,2.33]

print("---------alinea (a)------")
plt.plot(m, T,"ro") # coloca os pontos nos graficos
plt.xlabel('m(Kg)') # legenda no eixo dos x
plt.ylabel('T(K)') # legenda no eixo dos y
plt.title('Exercicio 7 MSF') #titulo do grafico
plt.show() #mostrar grafico 
print() 
#Resposta: Não é linear


print("---------alinea (b)------")
logt= np.log(T)
logm=np.log(m)
xmax=np.max(logm)*0.9
xmin=np.min(logm)*1.1

lin_reg = stats.linregress(logm, logt) #lista com o declive, ordenada, valor de r, ?, delta m, deltab 
x = np.linspace(xmin, xmax, 100)#Gerar array com 100 valores 
plt.plot(x, x * lin_reg.slope + lin_reg.intercept)
plt.plot(logm, logt, "ro")
plt.show()
#Resposta: São proporcionalmente diretos
print("Declive:{:.3f} +/- {:.3f} ".format(lin_reg.slope,lin_reg.stderr))
print("Ordenada na origem: {} +/- {} ".format(lin_reg.intercept,lin_reg.intercept_stderr))
print("Erro:", (lin_reg.rvalue **2))

print("---------alinea (c)------")

T_=[i**2 for i in T]
xmax=np.max(m)*1.1
xmin=np.min(m)*0.9

lin_reg = stats.linregress(m, T_) #lista com o declive, ordenada, valor de r, ?, delta m, deltab 
x = np.linspace(xmin, xmax, 100)#Gerar array com 100 valores 
plt.plot(x, x * lin_reg.slope + lin_reg.intercept)
plt.plot(m, T_, "ro")
plt.show()

print("Declive:{:.3f} +/- {:.3f} ".format(lin_reg.slope,lin_reg.stderr))
print("Ordenada na origem: {} +/- {} ".format(lin_reg.intercept,lin_reg.intercept_stderr))
print("Erro:", (lin_reg.rvalue **2))


print("---------alinea (d)------")
lin_reg = stats.linregress(logm, logt)
k=(2*np.pi/(np.e**lin_reg.intercept))**2
print(k,"+/- ",lin_reg.intercept_stderr)
#------esta a dar incorreto_------

#plt.show()


