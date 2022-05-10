mass = 75
miu = 0.004
Cres = 0.9
A = 0.30
dAr = 1.225
g = 9.80

v = 296.010*1000/3600

Rar = 0.5*Cres*A*dAr*(v**2)
N = mass*g
FAt = N*miu

P = (Rar + FAt)*v

print("A uma velocidade de {:.2f} m/s, o ciclista aplica uma potência de {:.2f} W.".format(v,P))