import math
import numpy as np
import matplotlib.pyplot as plt

x = [0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329]
N = len(x)
t = np.arange(0,N)


sumtixi = 0
for i in range(N):
    sumtixi = sumtixi + (t[i]*x[i])

sumti2 = 0
for i in range(N):
    sumti2 = sumti2+ (pow(t[i],2))

sumxi2 = 0
for i in range(N):
    sumxi2 = sumxi2+ (pow(x[i],2))

m = (N*sumtixi-sum(t)*sum(x))/(N*sumti2-pow(sum(t),2))
print("m =", str (m))

b = (sumti2*sum(x)-sum(t)*sumtixi)/(N*sumti2-pow(sum(t),2))
print("b =", str (b))

r2 = pow((N*sumtixi-sum(t)*sum(x)),2)/((N*sumti2-pow(sum(t),2))*(N*sumxi2-pow(sum(x),2)))
print("r2 =", str (r2), "logo é uma relação linear bem aproximada")

dm= abs(m)*math.sqrt(((1/r2)-1)/(N-2))
print("dm =", str (dm), "conseguiu mais ou menos manter a mesma velocidade uniforme")

db = dm*math.sqrt(sumti2/N)
print("db =", str (dm))

dp = x[N-1]-x[0]
vm = dp/(N-1)
print("vm =", str (vm), "km/min")

r = np.polyfit(t,x,1)
print("polyfit =", r ,"; os valores concordam com os valores de m e b!")

vmkmh = vm*60
print("vmkmh =", str (vmkmh), "km/h")

plt.plot(t,x,".")
plt.show()