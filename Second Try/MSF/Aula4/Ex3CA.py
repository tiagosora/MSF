# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:16:57 2022

@author: draki

Euler method:
    
t = np.linspace(T0, TF, N), T0= initial time; TF= final time; N= Number of total points (dont forget t0)
t = np.arange(T0, TF+dT, dT), T0= initial time; TF+dT= final time plus size of step due to last being exclusive; dT= Size of steps 

"""

from sympy import *
t, v, vt, g, D, a, aS = symbols('t v vt g D a aS')

v = integrate(9.8, t) # primitivaçao de uma funçao
vsimp = simplify(v)
print(vsimp) 

x = integrate(v, t) #primitivaçao de outra
xsimp = simplify(x)
print(xsimp)