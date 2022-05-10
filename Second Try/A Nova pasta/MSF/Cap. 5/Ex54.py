import numpy as np
import matplotlib.pyplot as plt
import math

dx = 0.002
b = 2
a = 0

N = np.int((b-a)/dx) + 1

x = np.zeros(N+1)
f = np.zeros(N)

for i in range(N):
    x[i+1] = x[i] + dx
    f[i] = (x[i]**3)/4

## Resolução
i = dx*((f[0] + f[N-1])*0.5 + np.sum(f[1:N-1])) ##Deve-se usar N-1 uma vez que este é o numero de fatias no calculo do integral
print("O integral dado é {}, com dt = {}.".format(i, dx))