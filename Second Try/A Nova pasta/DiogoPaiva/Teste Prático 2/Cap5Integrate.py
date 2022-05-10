import math

import matplotlib.pyplot as plt

import numpy as np

import sympy as sym

ValorEsperado = 1
x0 = 0                                                  # x inicial (debaixo no simbolo de integral)
xf = 2                                                  # x final (em cima no simbolo de integral)
dx = 0.01                                               
N = np.int((xf/dx))                                 
x = np.linspace(x0,xf,N+1)
f = np.empty(N+1)


for i in range(N):                                       # Todos os valores de dx em dx da função
    f[i] = (x[i]**3)/4                                   # A função que queremos integrar


integral = (((f[0]+f[N])/2)+np.sum(f[1:N-1]))*dx         #Fórmula para integração
erro = abs(ValorEsperado-integral)                       #Erro (se derem valor esperado)

print(integral)
print(erro)