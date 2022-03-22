import numpy as np
import matplotlib.pyplot as plt

grav=9.80
vt=6.80
altura=20.0
# alinea a), b) e c)
tem=np.linspace(0,4,110)
y=vt**2/grav*np.log(np.cosh(grav/vt*tem))
vel=vt*np.tanh(grav*tem/vt)             # velocidade
ace=grav/np.cosh(grav*tem/vt)**2        # aceleracao

fig, ax = plt.subplots(1)   # faça as figuras para vel e ace
ax.set_ylabel( 'y (m)' )
ax.set_xlabel( 't (s)' )
plt.grid()
ax.plot(tem,ace)
ax.set_title( 'Queda Volante com vy(0)=0' )
#plt.savefig('Quedavolante_y.png',bbox_inches="tight")
plt.show()

# alinea e) e f)
ext=altura*grav/vt**2
ex=np.exp(ext)
gt=np.arccosh(ex)
tempo=gt*vt/grav
print('gt/vt= ',gt,'    tempo chegada ao solo = ',tempo)
temlivre=np.sqrt(2*altura/grav)
print(' tempo queda livre ao solo = ',temlivre)
veloc=vt*np.tanh(grav*tempo/vt)
print(' velocidade(solo) = ',veloc)
acele=grav/np.cosh(grav*tempo/vt)**2
print(' acelera(solo) = ',acele)