# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:48:25 2022

@author: draki


"""

from sympy import *

t, v, vt, g, D, a, aS = symbols('t v vt g D a aS')

vchange = integrate(-9.8, t)
print(vchange)

v = 10 + vchange

vwithTerminal = diff((((27.7778)**2/9.8)*ln(cosh((9.8*t)/27.7778))), t)
awithTerminal = diff(vwithTerminal, t)

VTsimp = simplify(vwithTerminal)
ATsimp = simplify(awithTerminal)
print(ATsimp)
print(VTsimp)
y = integrate(v, t)
ysimp = simplify(y)
print(ysimp)
# 100 km/ hour = 27.7778 m/s