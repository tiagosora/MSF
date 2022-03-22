import math
import numpy as np
import matplotlib.pyplot as plt

K = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
E = [0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7]

N = len(K)

# plt.plot(K,E,"ob")

logK = []
logE = []

for i in range(N):
    logK.append(math.log(K[i]))

for i in range(N):
    logE.append(math.log(E[i]))

print(np.polyfit(logK,logE,1))

plt.plot(logK,logE)
plt.show()