import numpy as np
import matplotlib.pyplot as plt

ap=2                        # m/s**2  aceleração do carro patrulha
vx0a=70                     # km/h  velocidade inicial do carro A
vx0a=vx0a/3.6               # m/s   conversão ad velocidade para m/s
vx0p=0
tempo=np.linspace(0,30,1000)    # criação de um vetor do tempo
xa=vx0a*tempo               # movimento uniforme carro A
xp=0.5*ap*tempo**2          # movimento uniformente acelerado carro patrulha       

# a)
fig, ax = plt.subplots(1)
ax.set_xlabel( 'tempo (s)' )
ax.set_ylabel( 'x (m)' )
ax.plot(tempo,xa,label='Carro A')
ax.plot(tempo,xp,label='Carro Patrulha')
ax.set_title( 'Dois Carros' )
plt.legend()
plt.grid()
plt.savefig('DoisCarros.png',bbox_inches="tight")

# b)
tenc=2*vx0a/ap           # xa=xp instante de encontro
xenc=vx0a*tenc
print('tempo encontro = ',tenc)
print('posição encontro = ',xenc)