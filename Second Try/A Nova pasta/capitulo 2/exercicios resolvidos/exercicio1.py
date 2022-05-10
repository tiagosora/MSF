import matplotlib.pyplot as plt 
import numpy as np

t = np.linspace(0,30,100) #lista do intervalos de tempo
velocidadea= 70/3.6 # velocidade do carro A em m/s
aceleraçaob=2 #aceleração do carro de patrulha
x1= velocidadea*t # mov. uniforme do carro A
x2 = aceleraçaob*0.5* t**2 #mov. uniformemente acelerado do carro patrulha

print("---------alinea (a)------")
fig, ax = plt.subplots(1)
ax.set_xlabel('tempo (s)')
ax.set_ylabel('x (m)')
plt.plot(t, x1, label = 'Carro A')
plt.plot(t, x2, label = 'Carro Patrulha')
ax.set_title('Dois Carros') #titulo do grafico
plt.legend()
plt.grid()
plt.show() #mostrar grafico 

print("---------alinea (b)------")
t=2*velocidadea /aceleraçaob #instante encontro 
x= ((velocidadea**2) *2) /aceleraçaob #posição de encontro
print("{:.0f} s e {:.0f} m".format(t,x))

