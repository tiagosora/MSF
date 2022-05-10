import numpy as np
import matplotlib.pyplot as plt

xi=0
xf=2
dx=0.001
n=np.int(xf/dx +0.1)
valorEsperado = 1

x=np.linspace(xi, xf, n+1)
fun=np.empty(n+1)
int_trab_res=np.empty(n+1)

for i in range(0,n):
    fun[i]= x[i]**3 /4

integral=dx*((fun[0]-fun[n])*0.5+ np.sum(fun[1]))
erro= abs(valorEsperado*integral)
print(integral)
print(erro)
