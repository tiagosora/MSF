# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:44:03 2022

@author: draki
"""

from sympy import *
t, v, vt, g, D, a, aS = symbols('t v vt g D a aS') # definiçao de variaveis no sympy
v = diff((vt*vt)/g * log(cosh((g*t)/vt)), t)  # derivada da equaçao de posiçao
a = diff(vt*sinh(g*t/vt)/cosh(g*t/vt), t) # derivada da equaçao de velocidade
v = simplify(v) # simplificação da equaçao
print(v)
a = simplify(a) # simplificação da equaçao
print(a)