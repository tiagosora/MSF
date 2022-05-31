import matplotlib.pyplot as plt
import numpy as np

x = np.array([222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0])
y = np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])
N = x.size

xy = x*y
xx = np.square(x)
yy = np.square(y)

Sumx = x.sum() # Somatorio de x
Sumy = y.sum() # Somatorio de y
Sumxy = xy.sum() # Somatorio de x*y
Sumxx = xx.sum() # Somatorio de x^2
Sumyy = yy.sum() # Somatorio de y^2

m = ((N * Sumxy) - (Sumx * Sumy))/(N * Sumxx - (Sumx)**2) # Declive da reta de regressão linear

b = ((Sumxx * Sumy) - (Sumx * Sumxy))/(N * Sumxx - (Sumx)**2) # coordenada na origem da reta de regressão linear

r2_top_numerator = ((N*Sumxy) - (Sumx*Sumy))**2 # parte de cima da divisão do r^2 
r2_top_denominator = ((N*Sumxx)-(Sumx)**2)*((N*Sumyy) - (Sumy)**2) # parte de baixo da divisão do r^2

r2 = r2_top_numerator/r2_top_denominator # calculo do r^2

deltamSquareroot = np.sqrt(((1/r2)-1)/(N-2)) # parte da raiz do erro associado ao declive
deltam = abs(m)*deltamSquareroot # erro associado ao declive ou seja m +- deltam

print(deltam) 

deltabSquareroot = np.sqrt(Sumxx/N) # parte da raiz do erro associado ao declive
deltab = deltam * deltabSquareroot # erro associado á coordenada na origem, b +- deltab 

#PLOT

xmax = np.max(x)*1.1 # valor maximo de x para dar display no grafico
xmin = np.min(x)*0.9 # valor min de x...
ymax = np.max(y)*1.1 # valor maximo de y para dar display no grafico
ymin = np.min(y)*0.9 # valor min de y..
x1 = np.array([xmin,xmax]) # valores para inserir na reta da regressao linear, o min e max sao suficientes devido aos limite do grafico e 
                           # ser um reta linear;
yline = m*x1+b # calculo dos y da regressão linear

print(m*165+b) # print do valor de y quando x = 165
print(r2) # print do coeficiente de determinação 

fig1, ax = plt.subplots(1, 2, figsize=(13,6), layout="constrained") # definir dois graficos

ax[0].plot(x,y,"o") # inserir x e y no grafico
ax[0].set_xlim([xmin,xmax]) # definir limites
ax[0].set_ylim([ymin,ymax]) # ^

ax[1].plot(x,y,"o",x1,yline) # inserir x e y no grafico com a reta da regressao linear (x1, yline)

ax[1].set_xlim([xmin,xmax]) # definir limites
ax[1].set_ylim([ymin,ymax]) # definir limites





