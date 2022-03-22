import math
import numpy as np
import matplotlib.pyplot as plt

x = [222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0]
y = [2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0]

N = len(x); #ou len(y)

# plt.plot(x,y,".")
# plt.show()

sumxiyi = 0
for i in range(N):
    sumxiyi = sumxiyi + (x[i]*y[i])

sumxi2 = 0
for i in range(N):
    sumxi2 = sumxi2+ (pow(x[i],2))

sumyi2 = 0
for i in range(N):
    sumyi2 = sumyi2+ (pow(y[i],2))

m = (N*sumxiyi-sum(x)*sum(y))/(N*sumxi2-pow(sum(x),2))
print("m =", str (m))

b = (sumxi2*sum(y)-sum(x)*sumxiyi)/(N*sumxi2-pow(sum(x),2))
print("b =", str (b))

r2 = pow((N*sumxiyi-sum(x)*sum(y)),2)/((N*sumxi2-pow(sum(x),2))*(N*sumyi2-pow(sum(y),2)))
print("r2 =", str (r2))

dm= abs(m)*math.sqrt(((1/r2)-1)/(N-2))
print("dm =", str (dm))

db = dm*math.sqrt(sumxi2/N)
print("db =", str (dm))

print("Declive (m) = "+str(m))
print("Ordenada na origem (b) = "+str(b))
print("Coeficiente de determinação ou de correlação (r2) = "+str(r2))

yD = []
for i in range(N):
    yD.append(m*x[i]+b)

xE = m*165 + b
print("X cujo L = 165 : ",xE);

# plt.plot(x,y,".")
# plt.plot(x,yD,"b")

# Removido o penultimo ponto de cada um dos x e y

x = [222.0, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0]
y = [2.3, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0]
N = len(x); #ou len(y)

m = (N*sumxiyi-sum(x)*sum(y))/(N*sumxi2-pow(sum(x),2))
print("m =", str (m))

b = (sumxi2*sum(y)-sum(x)*sumxiyi)/(N*sumxi2-pow(sum(x),2))
print("b =", str (b))

r2 = pow((N*sumxiyi-sum(x)*sum(y)),2)/((N*sumxi2-pow(sum(x),2))*(N*sumyi2-pow(sum(y),2)))
print("r2 =", str (r2))

yD = []
for i in range(N):
    yD.append(m*x[i]+b)

plt.plot(x,y,"ob")
plt.plot(x,yD,"r")
plt.show()