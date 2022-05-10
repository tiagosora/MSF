import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats


def grafico(x_values, y_values, x_name, y_name):  # (x_array, y_array, Ox_name, Oy_name)
    plt.plot(x_values, y_values, 'g')
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.grid(True)
    plt.show()


def comparadorGraficos(x1_values, y1_values, legenda1, x2_values, y2_values, legenda2, x_name, y_name):  # (
    # x_array_1, y_array_1, x_array_2, y_Array_2, Ox_name, Oy_name)
    plt.plot(x1_values, y1_values, 'g', label=legenda1)
    plt.plot(x2_values, y2_values, 'r', label=legenda2)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    plt.grid(True)
    plt.show()


def maximo(xm1, xm2, xm3, ym1, ym2, ym3):  # máximo pelo polinómio de Lagrange
    xab = xm1 - xm2
    xac = xm1 - xm3
    xbc = xm2 - xm3

    a = ym1 / (xab * xac)
    b = -ym2 / (xab * xbc)
    c = ym3 / (xac * xbc)

    xmla = (b + c) * xm1 + (a + c) * xm2 + (a + b) * xm3
    xmax = 0.5 * xmla / (a + b + c)

    xta = xmax - xm1
    xtb = xmax - xm2
    xtc = xmax - xm3

    ymax = a * xtb * xtc + b * xta * xtc + c * xta * xtb
    return xmax, ymax


def zerosv(xm1, xm2, xm3, ym1, ym2, ym3):  # raiz pelo polinómio de Lagrange
    xab = xm1 - xm2
    xac = xm1 - xm3
    xbc = xm2 - xm3

    a = ym1 / (xab * xac)
    b = -ym2 / (xab * xbc)
    c = ym3 / (xac * xbc)

    am = a + b + c
    bm = a * (xm2 + xm3) + b * (xm1 + xm3) + c * (xm1 + xm2)
    cm = a * xm2 * xm3 + b * xm1 * xm3 + c * xm1 * xm2

    xzero = (bm + np.sqrt(bm * bm - 4 * am * cm)) / (2 * am)
    if xm3 > xm1 and (xzero < xm1 or xzero > xm3):
        xzero = (bm - np.sqrt(bm * bm - 4 * am * cm)) / (2 * am)

    if xm1 > xm3 and (xzero < xm3 or xzero > xm1):
        xzero = (bm - np.sqrt(bm * bm - 4 * am * cm)) / (2 * am)

    xta = xzero - xm1
    xtb = xzero - xm2
    xtc = xzero - xm3
    yzero = a * xtb * xtc + b * xta * xtc + c * xta * xtb
    return xzero, yzero


# DADOS
g = 9.8
v0 = 200 / 3.6
vTerminal = 6.80
y0 = 0
vy0 = v0

dt = 0.01
ti = 0
tf = 5
numPassos = int((tf - ti) / dt)

t = np.zeros(numPassos + 1)
ay = np.zeros(numPassos + 1)
vy = np.zeros(numPassos + 1)
y = np.zeros(numPassos + 1)

D = g / vTerminal ** 2
t[0] = ti
vy[0] = v0  # sentido do eixo de cima para baixo
y[0] = y0

for c in range(numPassos):
    # tempos
    t[c + 1] = t[c] + dt

    # aceleracoes
    ay[c] = g - D * abs(vy[c]) * vy[c]

    # velocidades
    vy[c + 1] = vy[c] + ay[c] * dt

    # posicoes
    y[c + 1] = y[c] + vy[c] * dt

# A
grafico(t, y, 't(s)', 'y(m)')

# B
grafico(t, vy, 't(s)', 'vy(m/s)')

# C - velocidade ao fim de 1 segundo
for i in range(numPassos):
    if 1 - 2 * dt < t[i] < 1 + 2 * dt:
        print('t = {}    v = {}'.format(t[i], vy[i]))

for i in range(numPassos):
    if 4 - 0.5 < y[i] < 4 + 0.5:
        print('t = {}    y = {}'.format(t[i], y[i]))

# grafico a 2 dimensoes
plt.plot(x_, y_, label='metodo euler')
plt.plot(x, y, label='metodos analiticos')
plt.xlabel('y(m)')
plt.ylabel('t(s)')
plt.legend()
plt.grid(True)
plt.show()
